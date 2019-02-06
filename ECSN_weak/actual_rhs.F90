module actual_rhs_module

  use amrex_fort_module, only: rt => amrex_real
  use amrex_constants_module
  use physical_constants, only: N_AVO
  use network
  use table_rates
  use burn_type_module

  implicit none

  type :: rate_eval_t
     real(rt) :: unscreened_rates(4, nrates)
     real(rt) :: screened_rates(nrates)
     real(rt) :: add_energy(nrat_tabular)
     real(rt) :: add_energy_rate(nrat_tabular)
  end type rate_eval_t
  
contains

  subroutine actual_rhs_init()
    ! STUB FOR MAESTRO'S TEST_REACT. ALL THE INIT IS DONE BY BURNER_INIT
    return
  end subroutine actual_rhs_init


  subroutine update_unevolved_species(state)
    ! STUB FOR INTEGRATOR
    type(burn_t)     :: state

    !$gpu
    
    return
  end subroutine update_unevolved_species


  subroutine zero_rate_eval(rate_eval)

    implicit none

    type(rate_eval_t), intent(inout) :: rate_eval

    !$gpu

    rate_eval % unscreened_rates(i_rate, :) = ZERO
    rate_eval % unscreened_rates(i_drate_dt, :) = ZERO
    rate_eval % unscreened_rates(i_scor, :) = ONE
    rate_eval % unscreened_rates(i_dscor_dt, :) = ZERO
    rate_eval % screened_rates = ZERO
    rate_eval % add_energy = ZERO
    rate_eval % add_energy_rate = ZERO

  end subroutine zero_rate_eval


  subroutine evaluate_rates(state, rate_eval)
    !$acc routine seq

    use reaclib_rates, only: screen_reaclib, reaclib_evaluate
    use screening_module, only: screen5, plasma_state, fill_plasma_state

    implicit none
    
    type(burn_t)     :: state
    type(rate_eval_t), intent(out) :: rate_eval
    type(plasma_state) :: pstate
    real(rt) :: Y(nspec)
    real(rt) :: raw_rates(4, nrates)
    real(rt) :: reactvec(num_rate_groups+2)
    integer :: i, j
    real(rt) :: rhoy, scor, dscor_dt, dscor_dd

    !$gpu

    Y(:) = state % xn(:) * aion_inv(:)
    rhoy = state % rho * state % y_e

    ! Zero out the rates
    call zero_rate_eval(rate_eval)

    ! Calculate Reaclib rates
    call fill_plasma_state(pstate, state % T, state % rho, Y)
    do i = 1, nrat_reaclib
       call reaclib_evaluate(pstate, state % T, i, reactvec)
       rate_eval % unscreened_rates(:,i) = reactvec(1:4)
    end do

    ! Evaluate screening factors
    if (screen_reaclib) then

      call screen5(pstate, 1, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,4) = scor
      rate_eval % unscreened_rates(i_dscor_dt,4) = dscor_dt


      call screen5(pstate, 2, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,5) = scor
      rate_eval % unscreened_rates(i_dscor_dt,5) = dscor_dt
      rate_eval % unscreened_rates(i_scor,9) = scor
      rate_eval % unscreened_rates(i_dscor_dt,9) = dscor_dt


      call screen5(pstate, 3, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,6) = scor
      rate_eval % unscreened_rates(i_dscor_dt,6) = dscor_dt
      rate_eval % unscreened_rates(i_scor,7) = scor
      rate_eval % unscreened_rates(i_dscor_dt,7) = dscor_dt


      call screen5(pstate, 4, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,8) = scor
      rate_eval % unscreened_rates(i_dscor_dt,8) = dscor_dt

    end if

    ! Calculate tabular rates
    call tabular_evaluate(rate_table_j_f20_o20, rhoy_table_j_f20_o20, temp_table_j_f20_o20, &
                          num_rhoy_j_f20_o20, num_temp_j_f20_o20, num_vars_j_f20_o20, &
                          rhoy, state % T, reactvec)
    rate_eval % unscreened_rates(:,10) = reactvec(1:4)
    rate_eval % add_energy(1) = reactvec(5)
    rate_eval % add_energy_rate(1)  = reactvec(6)

    call tabular_evaluate(rate_table_j_ne20_f20, rhoy_table_j_ne20_f20, temp_table_j_ne20_f20, &
                          num_rhoy_j_ne20_f20, num_temp_j_ne20_f20, num_vars_j_ne20_f20, &
                          rhoy, state % T, reactvec)
    rate_eval % unscreened_rates(:,11) = reactvec(1:4)
    rate_eval % add_energy(2) = reactvec(5)
    rate_eval % add_energy_rate(2)  = reactvec(6)


    ! Compute screened rates
    rate_eval % screened_rates = rate_eval % unscreened_rates(i_rate, :) * &
                                 rate_eval % unscreened_rates(i_scor, :)

  end subroutine evaluate_rates


  subroutine actual_rhs(state)
    
    !$acc routine seq

    use extern_probin_module, only: do_constant_volume_burn
    use burn_type_module, only: net_itemp, net_ienuc
    use sneut_module, only: sneut5
    use temperature_integration_module, only: temperature_rhs

    implicit none

    type(burn_t) :: state
    type(rate_eval_t) :: rate_eval
    real(rt) :: Y(nspec), ydot_nuc(nspec)
    real(rt) :: reactvec(num_rate_groups+2)
    integer :: i, j
    real(rt) :: rhoy, ye, enuc
    real(rt) :: sneut, dsneutdt, dsneutdd, snuda, snudz

    !$gpu

    ! Set molar abundances
    Y(:) = state % xn(:) * aion_inv(:)

    call evaluate_rates(state, rate_eval)

    call rhs_nuc(state, ydot_nuc, Y, rate_eval % screened_rates)
    state % ydot(1:nspec) = ydot_nuc

    ! ion binding energy contributions
    call ener_gener_rate(ydot_nuc, enuc)

    ! additional per-reaction energies
    ! including Q-value modification and electron chemical potential
    enuc = enuc + N_AVO * state % ydot(jf20) * rate_eval % add_energy(j_f20_o20)
    enuc = enuc + N_AVO * state % ydot(jne20) * rate_eval % add_energy(j_ne20_f20)

    ! additional energy generation rates
    ! including gamma heating and reaction neutrino losses (non-thermal)
    enuc = enuc + N_AVO * Y(jf20) * rate_eval % add_energy_rate(j_f20_o20)
    enuc = enuc + N_AVO * Y(jne20) * rate_eval % add_energy_rate(j_ne20_f20)


    ! Get the thermal neutrino losses
    call sneut5(state % T, state % rho, state % abar, state % zbar, sneut, dsneutdt, dsneutdd, snuda, snudz)

    ! Append the energy equation (this is erg/g/s)
    state % ydot(net_ienuc) = enuc - sneut

    ! Append the temperature equation
    call temperature_rhs(state)

  end subroutine actual_rhs


  subroutine rhs_nuc(state, ydot_nuc, Y, screened_rates)

    !$acc routine seq

    implicit none

    type (burn_t), intent(in) :: state
    real(rt), intent(out) :: ydot_nuc(nspec)
    real(rt), intent(in)  :: Y(nspec)
    real(rt), intent(in)  :: screened_rates(nrates)

    !$gpu

    double precision :: scratch_0
    double precision :: scratch_1
    double precision :: scratch_2
    double precision :: scratch_3
    double precision :: scratch_4
    double precision :: scratch_5
    double precision :: scratch_6
    double precision :: scratch_7
    double precision :: scratch_8
    double precision :: scratch_9
    double precision :: scratch_10
    double precision :: scratch_11
    double precision :: scratch_12
    double precision :: scratch_13
    double precision :: scratch_14
    double precision :: scratch_15
    double precision :: scratch_16
    double precision :: scratch_17

    scratch_0 = Y(jhe4)*state % rho
    scratch_1 = screened_rates(k_he4_mg24__p_al27)*Y(jmg24)*scratch_0
    scratch_2 = Y(jo16)**2*state % rho
    scratch_3 = screened_rates(k_o16_o16__p_p31)*scratch_2
    scratch_4 = Y(jhe4)*Y(jsi28)*state % rho
    scratch_5 = screened_rates(k_he4_si28__p_p31)*scratch_4
    scratch_6 = 0.5d0*scratch_3 + scratch_5
    scratch_7 = screened_rates(k_ne20__he4_o16)*Y(jne20)
    scratch_8 = screened_rates(k_he4_al27__p31)*Y(jal27)*scratch_0
    scratch_9 = -scratch_8
    scratch_10 = -scratch_1
    scratch_11 = screened_rates(k_o16_o16__he4_si28)*scratch_2
    scratch_12 = screened_rates(k_he4_si28__s32)*scratch_4
    scratch_13 = 0.5d0*scratch_11 - scratch_12 - scratch_5
    scratch_14 = screened_rates(k_f20__o20)*Y(jf20)
    scratch_15 = screened_rates(k_o20__f20__weak__wc12)*Y(jo20)
    scratch_16 = screened_rates(k_ne20__f20)*Y(jne20)
    scratch_17 = screened_rates(k_f20__ne20__weak__wc12)*Y(jf20)

    ydot_nuc(jp) = ( &
      scratch_1 + scratch_6 &
       )

    ydot_nuc(jhe4) = ( &
      scratch_10 + scratch_13 + scratch_7 + scratch_9 &
       )

    ydot_nuc(jo16) = ( &
      -scratch_11 - scratch_3 + scratch_7 &
       )

    ydot_nuc(jo20) = ( &
      scratch_14 - scratch_15 &
       )

    ydot_nuc(jf20) = ( &
      -scratch_14 + scratch_15 + scratch_16 - scratch_17 &
       )

    ydot_nuc(jne20) = ( &
      -scratch_16 + scratch_17 - scratch_7 &
       )

    ydot_nuc(jmg24) = ( &
      scratch_10 &
       )

    ydot_nuc(jal27) = ( &
      scratch_1 + scratch_9 &
       )

    ydot_nuc(jsi28) = ( &
      scratch_13 &
       )

    ydot_nuc(jp31) = ( &
      scratch_6 + scratch_8 &
       )

    ydot_nuc(js32) = ( &
      scratch_12 &
       )


  end subroutine rhs_nuc


  subroutine actual_jac(state)

    !$acc routine seq

    use burn_type_module, only: net_itemp, net_ienuc
    use sneut_module, only: sneut5
    use temperature_integration_module, only: temperature_jac
    use jacobian_sparsity_module, only: get_jac_entry, set_jac_entry, set_jac_zero

    implicit none
    
    type(burn_t) :: state
    type(rate_eval_t) :: rate_eval
    real(rt) :: reactvec(num_rate_groups+2)
    real(rt) :: screened_rates_dt(nrates)
    real(rt) :: Y(nspec), yderivs(nspec)
    real(rt) :: ye, rhoy, b1, scratch
    real(rt) :: sneut, dsneutdt, dsneutdd, snuda, snudz
    integer  :: j, k

    !$gpu

    ! Set molar abundances
    Y(:) = state % xn(:) * aion_inv(:)
    
    call evaluate_rates(state, rate_eval)

    ! Zero out the Jacobian
    call set_jac_zero(state)

    ! Species Jacobian elements with respect to other species
    call jac_nuc(state, Y, rate_eval % screened_rates)

    ! Evaluate the species Jacobian elements with respect to temperature by
    ! calling the RHS using the temperature derivative of the screened rate
    screened_rates_dt = rate_eval % unscreened_rates(i_rate, :) * &
                        rate_eval % unscreened_rates(i_dscor_dt, :) + &
                        rate_eval % unscreened_rates(i_drate_dt, :) * &
                        rate_eval % unscreened_rates(i_scor, :)

    call rhs_nuc(state, yderivs, Y, screened_rates_dt)

    do k = 1, nspec
       call set_jac_entry(state, k, net_itemp, yderivs(k))
    enddo

    ! Energy generation rate Jacobian elements with respect to species
    do j = 1, nspec
       do k = 1, nspec
          call get_jac_entry(state, k, j, yderivs(k))
       enddo
       call ener_gener_rate(yderivs, scratch)
       call set_jac_entry(state, net_ienuc, j, scratch)
    enddo

    ! Account for the thermal neutrino losses
    call sneut5(state % T, state % rho, state % abar, state % zbar, sneut, dsneutdt, dsneutdd, snuda, snudz)

    do j = 1, nspec
       b1 = ((aion(j) - state % abar) * state % abar * snuda + (zion(j) - state % zbar) * state % abar * snudz)
       call get_jac_entry(state, net_ienuc, j, scratch)
       scratch = scratch - b1
       call set_jac_entry(state, net_ienuc, j, scratch)
    enddo

    ! Energy generation rate Jacobian element with respect to temperature
    do k = 1, nspec
       call get_jac_entry(state, k, net_itemp, yderivs(k))
    enddo
    call ener_gener_rate(yderivs, scratch)
    scratch = scratch - dsneutdt    
    call set_jac_entry(state, net_ienuc, net_itemp, scratch)

    ! Temperature Jacobian elements
    call temperature_jac(state)

  end subroutine actual_jac


  subroutine jac_nuc(state, Y, screened_rates)

    !$acc routine seq

    use jacobian_sparsity_module, only: set_jac_entry

    implicit none

    type(burn_t), intent(inout) :: state
    real(rt), intent(in)  :: Y(nspec)
    real(rt), intent(in)  :: screened_rates(nrates)
    real(rt) :: scratch

    double precision :: scratch_0
    double precision :: scratch_1
    double precision :: scratch_2
    double precision :: scratch_3
    double precision :: scratch_4
    double precision :: scratch_5
    double precision :: scratch_6
    double precision :: scratch_7
    double precision :: scratch_8
    double precision :: scratch_9
    double precision :: scratch_10
    double precision :: scratch_11
    double precision :: scratch_12
    double precision :: scratch_13
    double precision :: scratch_14
    double precision :: scratch_15
    double precision :: scratch_16
    double precision :: scratch_17
    double precision :: scratch_18
    double precision :: scratch_19
    double precision :: scratch_20
    double precision :: scratch_21

    !$gpu

    scratch_0 = screened_rates(k_he4_mg24__p_al27)*state % rho
    scratch_1 = Y(jmg24)*scratch_0
    scratch_2 = screened_rates(k_he4_si28__p_p31)*state % rho
    scratch_3 = Y(jsi28)*scratch_2
    scratch_4 = 1.0d0*Y(jo16)*state % rho
    scratch_5 = screened_rates(k_o16_o16__p_p31)*scratch_4
    scratch_6 = Y(jhe4)*scratch_0
    scratch_7 = Y(jhe4)*scratch_2
    scratch_8 = screened_rates(k_he4_al27__p31)*state % rho
    scratch_9 = Y(jal27)*scratch_8
    scratch_10 = -scratch_9
    scratch_11 = -scratch_1
    scratch_12 = screened_rates(k_he4_si28__s32)*state % rho
    scratch_13 = Y(jsi28)*scratch_12
    scratch_14 = -scratch_13 - scratch_3
    scratch_15 = screened_rates(k_o16_o16__he4_si28)*scratch_4
    scratch_16 = -scratch_6
    scratch_17 = Y(jhe4)*scratch_8
    scratch_18 = -scratch_17
    scratch_19 = Y(jhe4)*scratch_12
    scratch_20 = -scratch_19 - scratch_7
    scratch_21 = 2.0d0*Y(jo16)*state % rho

    scratch = (&
      scratch_1 + scratch_3 &
       )
    call set_jac_entry(state, jp, jhe4, scratch)

    scratch = (&
      scratch_5 &
       )
    call set_jac_entry(state, jp, jo16, scratch)

    scratch = (&
      scratch_6 &
       )
    call set_jac_entry(state, jp, jmg24, scratch)

    scratch = (&
      scratch_7 &
       )
    call set_jac_entry(state, jp, jsi28, scratch)

    scratch = (&
      scratch_10 + scratch_11 + scratch_14 &
       )
    call set_jac_entry(state, jhe4, jhe4, scratch)

    scratch = (&
      scratch_15 &
       )
    call set_jac_entry(state, jhe4, jo16, scratch)

    scratch = (&
      screened_rates(k_ne20__he4_o16) &
       )
    call set_jac_entry(state, jhe4, jne20, scratch)

    scratch = (&
      scratch_16 &
       )
    call set_jac_entry(state, jhe4, jmg24, scratch)

    scratch = (&
      scratch_18 &
       )
    call set_jac_entry(state, jhe4, jal27, scratch)

    scratch = (&
      scratch_20 &
       )
    call set_jac_entry(state, jhe4, jsi28, scratch)

    scratch = (&
      -screened_rates(k_o16_o16__he4_si28)*scratch_21 - screened_rates(k_o16_o16__p_p31)* &
      scratch_21 &
       )
    call set_jac_entry(state, jo16, jo16, scratch)

    scratch = (&
      screened_rates(k_ne20__he4_o16) &
       )
    call set_jac_entry(state, jo16, jne20, scratch)

    scratch = (&
      -screened_rates(k_o20__f20__weak__wc12) &
       )
    call set_jac_entry(state, jo20, jo20, scratch)

    scratch = (&
      screened_rates(k_f20__o20) &
       )
    call set_jac_entry(state, jo20, jf20, scratch)

    scratch = (&
      screened_rates(k_o20__f20__weak__wc12) &
       )
    call set_jac_entry(state, jf20, jo20, scratch)

    scratch = (&
      -screened_rates(k_f20__ne20__weak__wc12) - screened_rates(k_f20__o20) &
       )
    call set_jac_entry(state, jf20, jf20, scratch)

    scratch = (&
      screened_rates(k_ne20__f20) &
       )
    call set_jac_entry(state, jf20, jne20, scratch)

    scratch = (&
      screened_rates(k_f20__ne20__weak__wc12) &
       )
    call set_jac_entry(state, jne20, jf20, scratch)

    scratch = (&
      -screened_rates(k_ne20__f20) - screened_rates(k_ne20__he4_o16) &
       )
    call set_jac_entry(state, jne20, jne20, scratch)

    scratch = (&
      scratch_11 &
       )
    call set_jac_entry(state, jmg24, jhe4, scratch)

    scratch = (&
      scratch_16 &
       )
    call set_jac_entry(state, jmg24, jmg24, scratch)

    scratch = (&
      scratch_1 + scratch_10 &
       )
    call set_jac_entry(state, jal27, jhe4, scratch)

    scratch = (&
      scratch_6 &
       )
    call set_jac_entry(state, jal27, jmg24, scratch)

    scratch = (&
      scratch_18 &
       )
    call set_jac_entry(state, jal27, jal27, scratch)

    scratch = (&
      scratch_14 &
       )
    call set_jac_entry(state, jsi28, jhe4, scratch)

    scratch = (&
      scratch_15 &
       )
    call set_jac_entry(state, jsi28, jo16, scratch)

    scratch = (&
      scratch_20 &
       )
    call set_jac_entry(state, jsi28, jsi28, scratch)

    scratch = (&
      scratch_3 + scratch_9 &
       )
    call set_jac_entry(state, jp31, jhe4, scratch)

    scratch = (&
      scratch_5 &
       )
    call set_jac_entry(state, jp31, jo16, scratch)

    scratch = (&
      scratch_17 &
       )
    call set_jac_entry(state, jp31, jal27, scratch)

    scratch = (&
      scratch_7 &
       )
    call set_jac_entry(state, jp31, jsi28, scratch)

    scratch = (&
      scratch_13 &
       )
    call set_jac_entry(state, js32, jhe4, scratch)

    scratch = (&
      scratch_19 &
       )
    call set_jac_entry(state, js32, jsi28, scratch)


  end subroutine jac_nuc

end module actual_rhs_module
