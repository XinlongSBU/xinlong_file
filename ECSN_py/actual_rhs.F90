module actual_rhs_module

  use amrex_fort_module, only: rt => amrex_real
  use amrex_constants_module
  use physical_constants, only: N_AVO
  use network
  use table_rates
  use burn_type_module

  implicit none

  ! Indices into rate groups in the rate_eval_t type
  integer, parameter :: i_rate        = 1
  integer, parameter :: i_drate_dt    = 2
  integer, parameter :: i_scor        = 3
  integer, parameter :: i_dscor_dt    = 4

  type :: rate_eval_t
     real(rt) :: unscreened_rates(num_rate_groups, nrates)
     real(rt) :: screened_rates(nrates)
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
    integer :: i, j
    real(rt) :: rhoy
    real(rt) :: rate, drate_dt, edot_nu
    real(rt) :: scor, dscor_dt, dscor_dd

    !$gpu

    Y(:) = state % xn(:) * aion_inv(:)
    rhoy = state % rho * state % y_e

    ! Zero out the rates
    call zero_rate_eval(rate_eval)

    ! Calculate Reaclib rates
    call fill_plasma_state(pstate, state % T, state % rho, Y)
    do i = 1, nrat_reaclib
       call reaclib_evaluate(pstate, state % T, i, rate, drate_dt)
       rate_eval % unscreened_rates(i_rate, i) = rate
       rate_eval % unscreened_rates(i_drate_dt, i) = drate_dt
    end do

    ! Evaluate screening factors
    if (screen_reaclib) then

      call screen5(pstate, 1, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,9) = scor
      rate_eval % unscreened_rates(i_dscor_dt,9) = dscor_dt


      call screen5(pstate, 2, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,10) = scor
      rate_eval % unscreened_rates(i_dscor_dt,10) = dscor_dt


      call screen5(pstate, 3, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,11) = scor
      rate_eval % unscreened_rates(i_dscor_dt,11) = dscor_dt


      call screen5(pstate, 4, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,12) = scor
      rate_eval % unscreened_rates(i_dscor_dt,12) = dscor_dt
      rate_eval % unscreened_rates(i_scor,20) = scor
      rate_eval % unscreened_rates(i_dscor_dt,20) = dscor_dt


      call screen5(pstate, 5, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,13) = scor
      rate_eval % unscreened_rates(i_dscor_dt,13) = dscor_dt
      rate_eval % unscreened_rates(i_scor,22) = scor
      rate_eval % unscreened_rates(i_dscor_dt,22) = dscor_dt


      call screen5(pstate, 6, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,14) = scor
      rate_eval % unscreened_rates(i_dscor_dt,14) = dscor_dt


      call screen5(pstate, 7, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,15) = scor
      rate_eval % unscreened_rates(i_dscor_dt,15) = dscor_dt
      rate_eval % unscreened_rates(i_scor,23) = scor
      rate_eval % unscreened_rates(i_dscor_dt,23) = dscor_dt
      rate_eval % unscreened_rates(i_scor,24) = scor
      rate_eval % unscreened_rates(i_dscor_dt,24) = dscor_dt


      call screen5(pstate, 8, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,16) = scor
      rate_eval % unscreened_rates(i_dscor_dt,16) = dscor_dt
      rate_eval % unscreened_rates(i_scor,25) = scor
      rate_eval % unscreened_rates(i_dscor_dt,25) = dscor_dt
      rate_eval % unscreened_rates(i_scor,26) = scor
      rate_eval % unscreened_rates(i_dscor_dt,26) = dscor_dt


      call screen5(pstate, 9, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,17) = scor
      rate_eval % unscreened_rates(i_dscor_dt,17) = dscor_dt
      rate_eval % unscreened_rates(i_scor,18) = scor
      rate_eval % unscreened_rates(i_dscor_dt,18) = dscor_dt


      call screen5(pstate, 10, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,19) = scor
      rate_eval % unscreened_rates(i_dscor_dt,19) = dscor_dt


      call screen5(pstate, 11, scor, dscor_dt, dscor_dd)
      rate_eval % unscreened_rates(i_scor,21) = scor
      rate_eval % unscreened_rates(i_dscor_dt,21) = dscor_dt

    end if

    ! Calculate tabular rates
    call tabular_evaluate(rate_table_j_f20_o20, rhoy_table_j_f20_o20, temp_table_j_f20_o20, &
                          num_rhoy_j_f20_o20, num_temp_j_f20_o20, num_vars_j_f20_o20, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,27) = rate
    rate_eval % unscreened_rates(i_drate_dt,27) = drate_dt
    rate_eval % add_energy_rate(1)  = edot_nu

    call tabular_evaluate(rate_table_j_ne20_f20, rhoy_table_j_ne20_f20, temp_table_j_ne20_f20, &
                          num_rhoy_j_ne20_f20, num_temp_j_ne20_f20, num_vars_j_ne20_f20, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,28) = rate
    rate_eval % unscreened_rates(i_drate_dt,28) = drate_dt
    rate_eval % add_energy_rate(2)  = edot_nu

    call tabular_evaluate(rate_table_j_o20_f20, rhoy_table_j_o20_f20, temp_table_j_o20_f20, &
                          num_rhoy_j_o20_f20, num_temp_j_o20_f20, num_vars_j_o20_f20, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,29) = rate
    rate_eval % unscreened_rates(i_drate_dt,29) = drate_dt
    rate_eval % add_energy_rate(3)  = edot_nu

    call tabular_evaluate(rate_table_j_f20_ne20, rhoy_table_j_f20_ne20, temp_table_j_f20_ne20, &
                          num_rhoy_j_f20_ne20, num_temp_j_f20_ne20, num_vars_j_f20_ne20, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,30) = rate
    rate_eval % unscreened_rates(i_drate_dt,30) = drate_dt
    rate_eval % add_energy_rate(4)  = edot_nu

    call tabular_evaluate(rate_table_j_mg24_na24, rhoy_table_j_mg24_na24, temp_table_j_mg24_na24, &
                          num_rhoy_j_mg24_na24, num_temp_j_mg24_na24, num_vars_j_mg24_na24, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,31) = rate
    rate_eval % unscreened_rates(i_drate_dt,31) = drate_dt
    rate_eval % add_energy_rate(5)  = edot_nu

    call tabular_evaluate(rate_table_j_na24_mg24, rhoy_table_j_na24_mg24, temp_table_j_na24_mg24, &
                          num_rhoy_j_na24_mg24, num_temp_j_na24_mg24, num_vars_j_na24_mg24, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,32) = rate
    rate_eval % unscreened_rates(i_drate_dt,32) = drate_dt
    rate_eval % add_energy_rate(6)  = edot_nu

    call tabular_evaluate(rate_table_j_al27_mg27, rhoy_table_j_al27_mg27, temp_table_j_al27_mg27, &
                          num_rhoy_j_al27_mg27, num_temp_j_al27_mg27, num_vars_j_al27_mg27, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,33) = rate
    rate_eval % unscreened_rates(i_drate_dt,33) = drate_dt
    rate_eval % add_energy_rate(7)  = edot_nu

    call tabular_evaluate(rate_table_j_mg27_al27, rhoy_table_j_mg27_al27, temp_table_j_mg27_al27, &
                          num_rhoy_j_mg27_al27, num_temp_j_mg27_al27, num_vars_j_mg27_al27, &
                          rhoy, state % T, rate, drate_dt, edot_nu)
    rate_eval % unscreened_rates(i_rate,34) = rate
    rate_eval % unscreened_rates(i_drate_dt,34) = drate_dt
    rate_eval % add_energy_rate(8)  = edot_nu


    ! Compute screened rates
    rate_eval % screened_rates = rate_eval % unscreened_rates(i_rate, :) * &
                                 rate_eval % unscreened_rates(i_scor, :)

  end subroutine evaluate_rates


  subroutine actual_rhs(state, ydot)
    
    !$acc routine seq

    use extern_probin_module, only: do_constant_volume_burn, disable_thermal_neutrinos
    use burn_type_module, only: net_itemp, net_ienuc, neqs
    use sneut_module, only: sneut5
    use temperature_integration_module, only: temperature_rhs

    implicit none

    type(burn_t), intent(in) :: state
    real(rt), intent(inout) :: ydot(neqs)

    type(rate_eval_t) :: rate_eval
    real(rt) :: Y(nspec), ydot_nuc(nspec)
    integer :: i, j
    real(rt) :: rhoy, ye, enuc
    real(rt) :: sneut, dsneutdt, dsneutdd, snuda, snudz

    !$gpu

    ! Set molar abundances
    Y(:) = state % xn(:) * aion_inv(:)

    call evaluate_rates(state, rate_eval)

    call rhs_nuc(state, ydot_nuc, Y, rate_eval % screened_rates)
    ydot(1:nspec) = ydot_nuc

    ! ion binding energy contributions
    call ener_gener_rate(ydot_nuc, enuc)

    ! include reaction neutrino losses (non-thermal)
    enuc = enuc + N_AVO * Y(jf20) * rate_eval % add_energy_rate(j_f20_o20)
    enuc = enuc + N_AVO * Y(jne20) * rate_eval % add_energy_rate(j_ne20_f20)
    enuc = enuc + N_AVO * Y(jo20) * rate_eval % add_energy_rate(j_o20_f20)
    enuc = enuc + N_AVO * Y(jf20) * rate_eval % add_energy_rate(j_f20_ne20)
    enuc = enuc + N_AVO * Y(jmg24) * rate_eval % add_energy_rate(j_mg24_na24)
    enuc = enuc + N_AVO * Y(jna24) * rate_eval % add_energy_rate(j_na24_mg24)
    enuc = enuc + N_AVO * Y(jal27) * rate_eval % add_energy_rate(j_al27_mg27)
    enuc = enuc + N_AVO * Y(jmg27) * rate_eval % add_energy_rate(j_mg27_al27)

    ! Get the thermal neutrino losses
    if (.not. disable_thermal_neutrinos) then
       call sneut5(state % T, state % rho, state % abar, state % zbar, sneut, dsneutdt, dsneutdd, snuda, snudz)
    else
       sneut = ZERO
    end if

    ! Append the energy equation (this is erg/g/s)
    ydot(net_ienuc) = enuc - sneut

    ! Append the temperature equation
    call temperature_rhs(state, ydot)

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
    double precision :: scratch_18
    double precision :: scratch_19
    double precision :: scratch_20
    double precision :: scratch_21
    double precision :: scratch_22
    double precision :: scratch_23
    double precision :: scratch_24
    double precision :: scratch_25
    double precision :: scratch_26
    double precision :: scratch_27
    double precision :: scratch_28
    double precision :: scratch_29
    double precision :: scratch_30
    double precision :: scratch_31
    double precision :: scratch_32
    double precision :: scratch_33
    double precision :: scratch_34
    double precision :: scratch_35
    double precision :: scratch_36
    double precision :: scratch_37
    double precision :: scratch_38
    double precision :: scratch_39
    double precision :: scratch_40
    double precision :: scratch_41
    double precision :: scratch_42
    double precision :: scratch_43
    double precision :: scratch_44
    double precision :: scratch_45
    double precision :: scratch_46
    double precision :: scratch_47
    double precision :: scratch_48
    double precision :: scratch_49
    double precision :: scratch_50

    scratch_0 = Y(jhe4)*state % rho
    scratch_1 = screened_rates(k_he4_na24__p_mg27)*Y(jna24)*scratch_0
    scratch_2 = Y(jp)*state % rho
    scratch_3 = screened_rates(k_p_mg27__he4_na24)*Y(jmg27)*scratch_2
    scratch_4 = scratch_1 - scratch_3
    scratch_5 = screened_rates(k_si28__p_al27)*Y(jsi28)
    scratch_6 = Y(jmg24)*scratch_0
    scratch_7 = screened_rates(k_he4_mg24__p_al27)*scratch_6
    scratch_8 = Y(jal27)*scratch_2
    scratch_9 = screened_rates(k_p_al27__he4_mg24)*scratch_8
    scratch_10 = screened_rates(k_p_al27__si28)*scratch_8
    scratch_11 = -scratch_10 + scratch_5 + scratch_7 - scratch_9
    scratch_12 = screened_rates(k_s32__p_p31)*Y(js32)
    scratch_13 = Y(jo16)**2*state % rho
    scratch_14 = screened_rates(k_o16_o16__p_p31)*scratch_13
    scratch_15 = Y(jsi28)*scratch_0
    scratch_16 = screened_rates(k_he4_si28__p_p31)*scratch_15
    scratch_17 = Y(jp31)*scratch_2
    scratch_18 = screened_rates(k_p_p31__he4_si28)*scratch_17
    scratch_19 = screened_rates(k_p_p31__o16_o16)*scratch_17
    scratch_20 = screened_rates(k_p_p31__s32)*scratch_17
    scratch_21 = scratch_12 + 0.5e0_rt*scratch_14 + scratch_16 - scratch_18 - scratch_19 - &
      scratch_20
    scratch_22 = screened_rates(k_ne20__he4_o16)*Y(jne20)
    scratch_23 = screened_rates(k_he4_o16__ne20)*Y(jo16)*scratch_0
    scratch_24 = scratch_22 - scratch_23
    scratch_25 = screened_rates(k_na24__he4_f20)*Y(jna24)
    scratch_26 = screened_rates(k_he4_f20__na24)*Y(jf20)*scratch_0
    scratch_27 = scratch_25 - scratch_26
    scratch_28 = screened_rates(k_mg24__he4_ne20)*Y(jmg24)
    scratch_29 = screened_rates(k_he4_ne20__mg24)*Y(jne20)*scratch_0
    scratch_30 = scratch_28 - scratch_29
    scratch_31 = -scratch_1 + scratch_3
    scratch_32 = screened_rates(k_si28__he4_mg24)*Y(jsi28)
    scratch_33 = screened_rates(k_he4_mg24__si28)*scratch_6
    scratch_34 = scratch_32 - scratch_33 - scratch_7 + scratch_9
    scratch_35 = screened_rates(k_p31__he4_al27)*Y(jp31)
    scratch_36 = screened_rates(k_he4_al27__p31)*Y(jal27)*scratch_0
    scratch_37 = scratch_35 - scratch_36
    scratch_38 = screened_rates(k_s32__he4_si28)*Y(js32)
    scratch_39 = screened_rates(k_o16_o16__he4_si28)*scratch_13
    scratch_40 = screened_rates(k_he4_si28__o16_o16)*scratch_15
    scratch_41 = screened_rates(k_he4_si28__s32)*scratch_15
    scratch_42 = -scratch_16 + scratch_18 + scratch_38 + 0.5e0_rt*scratch_39 - scratch_40 - &
      scratch_41
    scratch_43 = screened_rates(k_f20__o20)*Y(jf20)
    scratch_44 = screened_rates(k_o20__f20)*Y(jo20)
    scratch_45 = screened_rates(k_ne20__f20)*Y(jne20)
    scratch_46 = screened_rates(k_f20__ne20)*Y(jf20)
    scratch_47 = screened_rates(k_mg24__na24)*Y(jmg24)
    scratch_48 = screened_rates(k_na24__mg24)*Y(jna24)
    scratch_49 = screened_rates(k_al27__mg27)*Y(jal27)
    scratch_50 = screened_rates(k_mg27__al27)*Y(jmg27)

    ydot_nuc(jp) = ( &
      scratch_11 + scratch_21 + scratch_4 &
       )

    ydot_nuc(jhe4) = ( &
      scratch_24 + scratch_27 + scratch_30 + scratch_31 + scratch_34 + &
      scratch_37 + scratch_42 &
       )

    ydot_nuc(jo16) = ( &
      -scratch_14 + 2.0e0_rt*scratch_19 + scratch_24 - scratch_39 + 2.0e0_rt* &
      scratch_40 &
       )

    ydot_nuc(jo20) = ( &
      scratch_43 - scratch_44 &
       )

    ydot_nuc(jf20) = ( &
      scratch_27 - scratch_43 + scratch_44 + scratch_45 - scratch_46 &
       )

    ydot_nuc(jne20) = ( &
      -scratch_22 + scratch_23 + scratch_30 - scratch_45 + scratch_46 &
       )

    ydot_nuc(jna24) = ( &
      -scratch_25 + scratch_26 + scratch_31 + scratch_47 - scratch_48 &
       )

    ydot_nuc(jmg24) = ( &
      -scratch_28 + scratch_29 + scratch_34 - scratch_47 + scratch_48 &
       )

    ydot_nuc(jmg27) = ( &
      scratch_4 + scratch_49 - scratch_50 &
       )

    ydot_nuc(jal27) = ( &
      scratch_11 + scratch_37 - scratch_49 + scratch_50 &
       )

    ydot_nuc(jsi28) = ( &
      scratch_10 - scratch_32 + scratch_33 + scratch_42 - scratch_5 &
       )

    ydot_nuc(jp31) = ( &
      scratch_21 - scratch_35 + scratch_36 &
       )

    ydot_nuc(js32) = ( &
      -scratch_12 + scratch_20 - scratch_38 + scratch_41 &
       )


  end subroutine rhs_nuc


  subroutine actual_jac(state, jac)

    !$acc routine seq

    use burn_type_module, only: net_itemp, net_ienuc, neqs, njrows, njcols
    use extern_probin_module, only: disable_thermal_neutrinos
    use sneut_module, only: sneut5
    use temperature_integration_module, only: temperature_jac
    use jacobian_sparsity_module, only: get_jac_entry, set_jac_entry, set_jac_zero

    implicit none
    
    type(burn_t), intent(in) :: state
    real(rt), intent(inout) :: jac(njrows, njcols)

    type(rate_eval_t) :: rate_eval
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
    call set_jac_zero(jac)

    ! Species Jacobian elements with respect to other species
    call jac_nuc(state, jac, Y, rate_eval % screened_rates)

    ! Evaluate the species Jacobian elements with respect to temperature by
    ! calling the RHS using the temperature derivative of the screened rate
    screened_rates_dt = rate_eval % unscreened_rates(i_rate, :) * &
                        rate_eval % unscreened_rates(i_dscor_dt, :) + &
                        rate_eval % unscreened_rates(i_drate_dt, :) * &
                        rate_eval % unscreened_rates(i_scor, :)

    call rhs_nuc(state, yderivs, Y, screened_rates_dt)

    do k = 1, nspec
       call set_jac_entry(jac, k, net_itemp, yderivs(k))
    enddo

    ! Energy generation rate Jacobian elements with respect to species
    do j = 1, nspec
       do k = 1, nspec
          call get_jac_entry(jac, k, j, yderivs(k))
       enddo
       call ener_gener_rate(yderivs, scratch)
       call set_jac_entry(jac, net_ienuc, j, scratch)
    enddo

    ! Account for the thermal neutrino losses
    if (.not. disable_thermal_neutrinos) then
       call sneut5(state % T, state % rho, state % abar, state % zbar, sneut, dsneutdt, dsneutdd, snuda, snudz)

       do j = 1, nspec
          b1 = (-state % abar * state % abar * snuda + (zion(j) - state % zbar) * state % abar * snudz)
          call get_jac_entry(jac, net_ienuc, j, scratch)
          scratch = scratch - b1
          call set_jac_entry(jac, net_ienuc, j, scratch)
       enddo
    endif

    ! Energy generation rate Jacobian element with respect to temperature
    do k = 1, nspec
       call get_jac_entry(jac, k, net_itemp, yderivs(k))
    enddo
    call ener_gener_rate(yderivs, scratch)
    if (.not. disable_thermal_neutrinos) then
       scratch = scratch - dsneutdt
    endif
    call set_jac_entry(jac, net_ienuc, net_itemp, scratch)

    ! Temperature Jacobian elements
    call temperature_jac(state, jac)

  end subroutine actual_jac


  subroutine jac_nuc(state, jac, Y, screened_rates)

    !$acc routine seq

    use jacobian_sparsity_module, only: set_jac_entry

    implicit none

    type(burn_t), intent(in) :: state
    real(rt), intent(inout) :: jac(njrows, njcols)

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
    double precision :: scratch_22
    double precision :: scratch_23
    double precision :: scratch_24
    double precision :: scratch_25
    double precision :: scratch_26
    double precision :: scratch_27
    double precision :: scratch_28
    double precision :: scratch_29
    double precision :: scratch_30
    double precision :: scratch_31
    double precision :: scratch_32
    double precision :: scratch_33
    double precision :: scratch_34
    double precision :: scratch_35
    double precision :: scratch_36
    double precision :: scratch_37
    double precision :: scratch_38
    double precision :: scratch_39
    double precision :: scratch_40
    double precision :: scratch_41
    double precision :: scratch_42
    double precision :: scratch_43
    double precision :: scratch_44
    double precision :: scratch_45
    double precision :: scratch_46
    double precision :: scratch_47
    double precision :: scratch_48
    double precision :: scratch_49
    double precision :: scratch_50
    double precision :: scratch_51
    double precision :: scratch_52
    double precision :: scratch_53
    double precision :: scratch_54
    double precision :: scratch_55
    double precision :: scratch_56
    double precision :: scratch_57
    double precision :: scratch_58
    double precision :: scratch_59
    double precision :: scratch_60
    double precision :: scratch_61
    double precision :: scratch_62
    double precision :: scratch_63
    double precision :: scratch_64
    double precision :: scratch_65
    double precision :: scratch_66
    double precision :: scratch_67
    double precision :: scratch_68
    double precision :: scratch_69

    !$gpu

    scratch_0 = screened_rates(k_p_mg27__he4_na24)*state % rho
    scratch_1 = Y(jmg27)*scratch_0
    scratch_2 = -scratch_1
    scratch_3 = Y(jal27)*state % rho
    scratch_4 = screened_rates(k_p_al27__he4_mg24)*scratch_3
    scratch_5 = screened_rates(k_p_al27__si28)*scratch_3
    scratch_6 = -scratch_4 - scratch_5
    scratch_7 = Y(jp31)*state % rho
    scratch_8 = screened_rates(k_p_p31__he4_si28)*scratch_7
    scratch_9 = screened_rates(k_p_p31__o16_o16)*scratch_7
    scratch_10 = screened_rates(k_p_p31__s32)*scratch_7
    scratch_11 = -scratch_10 - scratch_8 - scratch_9
    scratch_12 = screened_rates(k_he4_mg24__p_al27)*state % rho
    scratch_13 = Y(jmg24)*scratch_12
    scratch_14 = screened_rates(k_he4_na24__p_mg27)*state % rho
    scratch_15 = Y(jna24)*scratch_14
    scratch_16 = screened_rates(k_he4_si28__p_p31)*state % rho
    scratch_17 = Y(jsi28)*scratch_16
    scratch_18 = Y(jo16)*state % rho
    scratch_19 = 1.0e0_rt*scratch_18
    scratch_20 = screened_rates(k_o16_o16__p_p31)*scratch_19
    scratch_21 = Y(jhe4)*scratch_14
    scratch_22 = Y(jhe4)*scratch_12
    scratch_23 = Y(jp)*scratch_0
    scratch_24 = -scratch_23
    scratch_25 = Y(jp)*state % rho
    scratch_26 = screened_rates(k_p_al27__he4_mg24)*scratch_25
    scratch_27 = screened_rates(k_p_al27__si28)*scratch_25
    scratch_28 = -scratch_26 - scratch_27
    scratch_29 = Y(jhe4)*scratch_16
    scratch_30 = screened_rates(k_p_p31__he4_si28)*scratch_25
    scratch_31 = screened_rates(k_p_p31__o16_o16)*scratch_25
    scratch_32 = screened_rates(k_p_p31__s32)*scratch_25
    scratch_33 = -scratch_30 - scratch_31 - scratch_32
    scratch_34 = screened_rates(k_he4_o16__ne20)*state % rho
    scratch_35 = Y(jo16)*scratch_34
    scratch_36 = -scratch_35
    scratch_37 = screened_rates(k_he4_ne20__mg24)*state % rho
    scratch_38 = Y(jne20)*scratch_37
    scratch_39 = -scratch_38
    scratch_40 = -scratch_15
    scratch_41 = screened_rates(k_he4_al27__p31)*scratch_3
    scratch_42 = -scratch_41
    scratch_43 = screened_rates(k_he4_f20__na24)*state % rho
    scratch_44 = Y(jf20)*scratch_43
    scratch_45 = -scratch_44
    scratch_46 = screened_rates(k_he4_mg24__si28)*state % rho
    scratch_47 = Y(jmg24)*scratch_46
    scratch_48 = -scratch_13 - scratch_47
    scratch_49 = Y(jsi28)*state % rho
    scratch_50 = screened_rates(k_he4_si28__o16_o16)*scratch_49
    scratch_51 = screened_rates(k_he4_si28__s32)*scratch_49
    scratch_52 = -scratch_17 - scratch_50 - scratch_51
    scratch_53 = Y(jhe4)*scratch_34
    scratch_54 = -scratch_53
    scratch_55 = screened_rates(k_o16_o16__he4_si28)*scratch_19
    scratch_56 = Y(jhe4)*scratch_43
    scratch_57 = -scratch_56
    scratch_58 = Y(jhe4)*scratch_37
    scratch_59 = -scratch_58
    scratch_60 = -scratch_21
    scratch_61 = Y(jhe4)*scratch_46
    scratch_62 = -scratch_22 - scratch_61
    scratch_63 = Y(jhe4)*state % rho
    scratch_64 = screened_rates(k_he4_al27__p31)*scratch_63
    scratch_65 = -scratch_64
    scratch_66 = screened_rates(k_he4_si28__o16_o16)*scratch_63
    scratch_67 = screened_rates(k_he4_si28__s32)*scratch_63
    scratch_68 = -scratch_29 - scratch_66 - scratch_67
    scratch_69 = 2.0e0_rt*scratch_18

    scratch = (&
      scratch_11 + scratch_2 + scratch_6 &
       )
    call set_jac_entry(jac, jp, jp, scratch)

    scratch = (&
      scratch_13 + scratch_15 + scratch_17 &
       )
    call set_jac_entry(jac, jp, jhe4, scratch)

    scratch = (&
      scratch_20 &
       )
    call set_jac_entry(jac, jp, jo16, scratch)

    scratch = (&
      scratch_21 &
       )
    call set_jac_entry(jac, jp, jna24, scratch)

    scratch = (&
      scratch_22 &
       )
    call set_jac_entry(jac, jp, jmg24, scratch)

    scratch = (&
      scratch_24 &
       )
    call set_jac_entry(jac, jp, jmg27, scratch)

    scratch = (&
      scratch_28 &
       )
    call set_jac_entry(jac, jp, jal27, scratch)

    scratch = (&
      screened_rates(k_si28__p_al27) + scratch_29 &
       )
    call set_jac_entry(jac, jp, jsi28, scratch)

    scratch = (&
      scratch_33 &
       )
    call set_jac_entry(jac, jp, jp31, scratch)

    scratch = (&
      screened_rates(k_s32__p_p31) &
       )
    call set_jac_entry(jac, jp, js32, scratch)

    scratch = (&
      scratch_1 + scratch_4 + scratch_8 &
       )
    call set_jac_entry(jac, jhe4, jp, scratch)

    scratch = (&
      scratch_36 + scratch_39 + scratch_40 + scratch_42 + scratch_45 + &
      scratch_48 + scratch_52 &
       )
    call set_jac_entry(jac, jhe4, jhe4, scratch)

    scratch = (&
      scratch_54 + scratch_55 &
       )
    call set_jac_entry(jac, jhe4, jo16, scratch)

    scratch = (&
      scratch_57 &
       )
    call set_jac_entry(jac, jhe4, jf20, scratch)

    scratch = (&
      screened_rates(k_ne20__he4_o16) + scratch_59 &
       )
    call set_jac_entry(jac, jhe4, jne20, scratch)

    scratch = (&
      screened_rates(k_na24__he4_f20) + scratch_60 &
       )
    call set_jac_entry(jac, jhe4, jna24, scratch)

    scratch = (&
      screened_rates(k_mg24__he4_ne20) + scratch_62 &
       )
    call set_jac_entry(jac, jhe4, jmg24, scratch)

    scratch = (&
      scratch_23 &
       )
    call set_jac_entry(jac, jhe4, jmg27, scratch)

    scratch = (&
      scratch_26 + scratch_65 &
       )
    call set_jac_entry(jac, jhe4, jal27, scratch)

    scratch = (&
      screened_rates(k_si28__he4_mg24) + scratch_68 &
       )
    call set_jac_entry(jac, jhe4, jsi28, scratch)

    scratch = (&
      screened_rates(k_p31__he4_al27) + scratch_30 &
       )
    call set_jac_entry(jac, jhe4, jp31, scratch)

    scratch = (&
      screened_rates(k_s32__he4_si28) &
       )
    call set_jac_entry(jac, jhe4, js32, scratch)

    scratch = (&
      2.0e0_rt*scratch_9 &
       )
    call set_jac_entry(jac, jo16, jp, scratch)

    scratch = (&
      scratch_36 + 2.0e0_rt*scratch_50 &
       )
    call set_jac_entry(jac, jo16, jhe4, scratch)

    scratch = (&
      -screened_rates(k_o16_o16__he4_si28)*scratch_69 - screened_rates(k_o16_o16__p_p31)* &
      scratch_69 + scratch_54 &
       )
    call set_jac_entry(jac, jo16, jo16, scratch)

    scratch = (&
      screened_rates(k_ne20__he4_o16) &
       )
    call set_jac_entry(jac, jo16, jne20, scratch)

    scratch = (&
      2.0e0_rt*scratch_66 &
       )
    call set_jac_entry(jac, jo16, jsi28, scratch)

    scratch = (&
      2.0e0_rt*scratch_31 &
       )
    call set_jac_entry(jac, jo16, jp31, scratch)

    scratch = (&
      -screened_rates(k_o20__f20) &
       )
    call set_jac_entry(jac, jo20, jo20, scratch)

    scratch = (&
      screened_rates(k_f20__o20) &
       )
    call set_jac_entry(jac, jo20, jf20, scratch)

    scratch = (&
      scratch_45 &
       )
    call set_jac_entry(jac, jf20, jhe4, scratch)

    scratch = (&
      screened_rates(k_o20__f20) &
       )
    call set_jac_entry(jac, jf20, jo20, scratch)

    scratch = (&
      -screened_rates(k_f20__ne20) - screened_rates(k_f20__o20) + scratch_57 &
       )
    call set_jac_entry(jac, jf20, jf20, scratch)

    scratch = (&
      screened_rates(k_ne20__f20) &
       )
    call set_jac_entry(jac, jf20, jne20, scratch)

    scratch = (&
      screened_rates(k_na24__he4_f20) &
       )
    call set_jac_entry(jac, jf20, jna24, scratch)

    scratch = (&
      scratch_35 + scratch_39 &
       )
    call set_jac_entry(jac, jne20, jhe4, scratch)

    scratch = (&
      scratch_53 &
       )
    call set_jac_entry(jac, jne20, jo16, scratch)

    scratch = (&
      screened_rates(k_f20__ne20) &
       )
    call set_jac_entry(jac, jne20, jf20, scratch)

    scratch = (&
      -screened_rates(k_ne20__f20) - screened_rates(k_ne20__he4_o16) + scratch_59 &
       )
    call set_jac_entry(jac, jne20, jne20, scratch)

    scratch = (&
      screened_rates(k_mg24__he4_ne20) &
       )
    call set_jac_entry(jac, jne20, jmg24, scratch)

    scratch = (&
      scratch_1 &
       )
    call set_jac_entry(jac, jna24, jp, scratch)

    scratch = (&
      scratch_40 + scratch_44 &
       )
    call set_jac_entry(jac, jna24, jhe4, scratch)

    scratch = (&
      scratch_56 &
       )
    call set_jac_entry(jac, jna24, jf20, scratch)

    scratch = (&
      -screened_rates(k_na24__he4_f20) - screened_rates(k_na24__mg24) + scratch_60 &
       )
    call set_jac_entry(jac, jna24, jna24, scratch)

    scratch = (&
      screened_rates(k_mg24__na24) &
       )
    call set_jac_entry(jac, jna24, jmg24, scratch)

    scratch = (&
      scratch_23 &
       )
    call set_jac_entry(jac, jna24, jmg27, scratch)

    scratch = (&
      scratch_4 &
       )
    call set_jac_entry(jac, jmg24, jp, scratch)

    scratch = (&
      scratch_38 + scratch_48 &
       )
    call set_jac_entry(jac, jmg24, jhe4, scratch)

    scratch = (&
      scratch_58 &
       )
    call set_jac_entry(jac, jmg24, jne20, scratch)

    scratch = (&
      screened_rates(k_na24__mg24) &
       )
    call set_jac_entry(jac, jmg24, jna24, scratch)

    scratch = (&
      -screened_rates(k_mg24__he4_ne20) - screened_rates(k_mg24__na24) + scratch_62 &
       )
    call set_jac_entry(jac, jmg24, jmg24, scratch)

    scratch = (&
      scratch_26 &
       )
    call set_jac_entry(jac, jmg24, jal27, scratch)

    scratch = (&
      screened_rates(k_si28__he4_mg24) &
       )
    call set_jac_entry(jac, jmg24, jsi28, scratch)

    scratch = (&
      scratch_2 &
       )
    call set_jac_entry(jac, jmg27, jp, scratch)

    scratch = (&
      scratch_15 &
       )
    call set_jac_entry(jac, jmg27, jhe4, scratch)

    scratch = (&
      scratch_21 &
       )
    call set_jac_entry(jac, jmg27, jna24, scratch)

    scratch = (&
      -screened_rates(k_mg27__al27) + scratch_24 &
       )
    call set_jac_entry(jac, jmg27, jmg27, scratch)

    scratch = (&
      screened_rates(k_al27__mg27) &
       )
    call set_jac_entry(jac, jmg27, jal27, scratch)

    scratch = (&
      scratch_6 &
       )
    call set_jac_entry(jac, jal27, jp, scratch)

    scratch = (&
      scratch_13 + scratch_42 &
       )
    call set_jac_entry(jac, jal27, jhe4, scratch)

    scratch = (&
      scratch_22 &
       )
    call set_jac_entry(jac, jal27, jmg24, scratch)

    scratch = (&
      screened_rates(k_mg27__al27) &
       )
    call set_jac_entry(jac, jal27, jmg27, scratch)

    scratch = (&
      -screened_rates(k_al27__mg27) + scratch_28 + scratch_65 &
       )
    call set_jac_entry(jac, jal27, jal27, scratch)

    scratch = (&
      screened_rates(k_si28__p_al27) &
       )
    call set_jac_entry(jac, jal27, jsi28, scratch)

    scratch = (&
      screened_rates(k_p31__he4_al27) &
       )
    call set_jac_entry(jac, jal27, jp31, scratch)

    scratch = (&
      scratch_5 + scratch_8 &
       )
    call set_jac_entry(jac, jsi28, jp, scratch)

    scratch = (&
      scratch_47 + scratch_52 &
       )
    call set_jac_entry(jac, jsi28, jhe4, scratch)

    scratch = (&
      scratch_55 &
       )
    call set_jac_entry(jac, jsi28, jo16, scratch)

    scratch = (&
      scratch_61 &
       )
    call set_jac_entry(jac, jsi28, jmg24, scratch)

    scratch = (&
      scratch_27 &
       )
    call set_jac_entry(jac, jsi28, jal27, scratch)

    scratch = (&
      -screened_rates(k_si28__he4_mg24) - screened_rates(k_si28__p_al27) + scratch_68 &
       )
    call set_jac_entry(jac, jsi28, jsi28, scratch)

    scratch = (&
      scratch_30 &
       )
    call set_jac_entry(jac, jsi28, jp31, scratch)

    scratch = (&
      screened_rates(k_s32__he4_si28) &
       )
    call set_jac_entry(jac, jsi28, js32, scratch)

    scratch = (&
      scratch_11 &
       )
    call set_jac_entry(jac, jp31, jp, scratch)

    scratch = (&
      scratch_17 + scratch_41 &
       )
    call set_jac_entry(jac, jp31, jhe4, scratch)

    scratch = (&
      scratch_20 &
       )
    call set_jac_entry(jac, jp31, jo16, scratch)

    scratch = (&
      scratch_64 &
       )
    call set_jac_entry(jac, jp31, jal27, scratch)

    scratch = (&
      scratch_29 &
       )
    call set_jac_entry(jac, jp31, jsi28, scratch)

    scratch = (&
      -screened_rates(k_p31__he4_al27) + scratch_33 &
       )
    call set_jac_entry(jac, jp31, jp31, scratch)

    scratch = (&
      screened_rates(k_s32__p_p31) &
       )
    call set_jac_entry(jac, jp31, js32, scratch)

    scratch = (&
      scratch_10 &
       )
    call set_jac_entry(jac, js32, jp, scratch)

    scratch = (&
      scratch_51 &
       )
    call set_jac_entry(jac, js32, jhe4, scratch)

    scratch = (&
      scratch_67 &
       )
    call set_jac_entry(jac, js32, jsi28, scratch)

    scratch = (&
      scratch_32 &
       )
    call set_jac_entry(jac, js32, jp31, scratch)

    scratch = (&
      -screened_rates(k_s32__he4_si28) - screened_rates(k_s32__p_p31) &
       )
    call set_jac_entry(jac, js32, js32, scratch)


  end subroutine jac_nuc

end module actual_rhs_module
