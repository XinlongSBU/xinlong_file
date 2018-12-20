module actual_rhs_module

  use bl_types
  use bl_constants_module
  use physical_constants, only: N_AVO
  use network
  use reaclib_rates, only: screen_reaclib, reaclib_evaluate
  use table_rates
  use screening_module, only: plasma_state, fill_plasma_state
  use sneut_module, only: sneut5
  use temperature_integration_module, only: temperature_rhs, temperature_jac
  use burn_type_module

  implicit none

  type :: rate_eval_t
     double precision :: unscreened_rates(4, nrates)
     double precision :: screened_rates(nrates)
     double precision :: dqweak(nrat_tabular)
     double precision :: epart(nrat_tabular)
  end type rate_eval_t
  
contains

  subroutine actual_rhs_init()
    ! STUB FOR MAESTRO'S TEST_REACT. ALL THE INIT IS DONE BY BURNER_INIT
    return
  end subroutine actual_rhs_init
  
  subroutine update_unevolved_species(state)
    ! STUB FOR INTEGRATOR
    type(burn_t)     :: state
    return
  end subroutine update_unevolved_species

  subroutine evaluate_rates(state, rate_eval)
    !$acc routine seq
    type(burn_t)     :: state
    type(rate_eval_t), intent(out) :: rate_eval
    type(plasma_state) :: pstate
    double precision :: Y(nspec)
    double precision :: raw_rates(4, nrates)
    double precision :: reactvec(num_rate_groups+2)
    integer :: i, j
    double precision :: dens, temp, rhoy

    Y(:) = state%xn(:) * aion_inv(:)
    dens = state%rho
    temp = state%T
    rhoy = dens*state%y_e
    
    ! Calculate Reaclib rates
    call fill_plasma_state(pstate, temp, dens, Y)
    do i = 1, nrat_reaclib
       call reaclib_evaluate(pstate, temp, i, reactvec)
       rate_eval % unscreened_rates(:,i) = reactvec(1:4)
    end do

    ! Included only if there are tabular rates
    do i = 1, nrat_tabular
      call tabular_evaluate(table_meta(i), rhoy, temp, reactvec)
      j = i + nrat_reaclib
      rate_eval % unscreened_rates(:,j) = reactvec(1:4)
      rate_eval % dqweak(i) = reactvec(5)
      rate_eval % epart(i)  = reactvec(6)
    end do

    ! Compute screened rates
    rate_eval % screened_rates = rate_eval % unscreened_rates(i_rate, :) * &
         rate_eval % unscreened_rates(i_scor, :)

  end subroutine evaluate_rates

  subroutine actual_rhs(state)
    
    !$acc routine seq

    use extern_probin_module, only: do_constant_volume_burn
    use burn_type_module, only: net_itemp, net_ienuc

    implicit none

    type(burn_t) :: state
    type(rate_eval_t) :: rate_eval
    type(plasma_state) :: pstate
    double precision :: Y(nspec)
    double precision :: ydot_nuc(nspec)
    double precision :: reactvec(num_rate_groups+2)
    integer :: i, j
    double precision :: dens, temp, rhoy, ye, enuc
    double precision :: sneut, dsneutdt, dsneutdd, snuda, snudz

    ! Set molar abundances
    Y(:) = state%xn(:) * aion_inv(:)

    dens = state%rho
    temp = state%T

    call evaluate_rates(state, rate_eval)

    call rhs_nuc(ydot_nuc, Y, rate_eval % screened_rates, dens)
    state%ydot(1:nspec) = ydot_nuc

    ! ion binding energy contributions
    call ener_gener_rate(ydot_nuc, enuc)
    
    ! weak Q-value modification dqweak (density and temperature dependent)
    enuc = enuc + N_AVO * state % ydot(jf20) * rate_eval % dqweak(j_f20_o20)
    enuc = enuc + N_AVO * state % ydot(jne20) * rate_eval % dqweak(j_ne20_f20)
    
    ! weak particle energy generation rates from gamma heating and neutrino loss
    ! (does not include plasma neutrino losses)
    enuc = enuc + N_AVO * Y(jf20) * rate_eval % epart(j_f20_o20)
    enuc = enuc + N_AVO * Y(jne20) * rate_eval % epart(j_ne20_f20)


    ! Get the neutrino losses
    call sneut5(temp, dens, state%abar, state%zbar, sneut, dsneutdt, dsneutdd, snuda, snudz)

    ! Append the energy equation (this is erg/g/s)
    state%ydot(net_ienuc) = enuc - sneut

    ! Append the temperature equation
    call temperature_rhs(state)
    
    ! write(*,*) '______________________________'
    ! do i = 1, nspec+2
    !    write(*,*) 'state%ydot(',i,'): ',state%ydot(i)
    ! end do
  end subroutine actual_rhs

  subroutine rhs_nuc(ydot_nuc, Y, screened_rates, dens)

    !$acc routine seq

    
    double precision, intent(out) :: ydot_nuc(nspec)
    double precision, intent(in)  :: Y(nspec)
    double precision, intent(in)  :: screened_rates(nrates)
    double precision, intent(in)  :: dens

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

    scratch_0 = Y(jhe4)*Y(jmg24)*dens
    scratch_1 = screened_rates(k_he4_mg24__p_al27)*scratch_0
    scratch_2 = Y(jal27)*Y(jp)*dens
    scratch_3 = screened_rates(k_p_al27__he4_mg24)*scratch_2
    scratch_4 = screened_rates(k_p_al27__si28)*scratch_2
    scratch_5 = scratch_1 - scratch_3 - scratch_4
    scratch_6 = Y(jo16)**2*dens
    scratch_7 = screened_rates(k_o16_o16__p_p31)*scratch_6
    scratch_8 = Y(jhe4)*Y(jsi28)*dens
    scratch_9 = screened_rates(k_he4_si28__p_p31)*scratch_8
    scratch_10 = Y(jp31)*Y(jp)*dens
    scratch_11 = screened_rates(k_p_p31__he4_si28)*scratch_10
    scratch_12 = screened_rates(k_p_p31__s32)*scratch_10
    scratch_13 = -scratch_11 - scratch_12 + 0.5d0*scratch_7 + scratch_9
    scratch_14 = screened_rates(k_ne20__he4_o16)*Y(jne20)
    scratch_15 = Y(jhe4)*dens
    scratch_16 = screened_rates(k_he4_al27__p31)*Y(jal27)*scratch_15
    scratch_17 = -scratch_16
    scratch_18 = -scratch_1
    scratch_19 = screened_rates(k_he4_mg24__si28)*scratch_0
    scratch_20 = -scratch_19
    scratch_21 = screened_rates(k_he4_ne20__mg24)*Y(jne20)*scratch_15
    scratch_22 = -scratch_21
    scratch_23 = screened_rates(k_he4_o16__ne20)*Y(jo16)*scratch_15
    scratch_24 = -scratch_23
    scratch_25 = screened_rates(k_o16_o16__he4_si28)*scratch_6
    scratch_26 = screened_rates(k_he4_si28__s32)*scratch_8
    scratch_27 = scratch_11 + 0.5d0*scratch_25 - scratch_26 - scratch_9
    scratch_28 = screened_rates(k_f20__o20)*Y(jf20)
    scratch_29 = screened_rates(k_o20__f20)*Y(jo20)
    scratch_30 = screened_rates(k_ne20__f20)*Y(jne20)
    scratch_31 = screened_rates(k_f20__ne20)*Y(jf20)

    ydot_nuc(jp) = ( &
      scratch_13 + scratch_5 &
       )

    ydot_nuc(jhe4) = ( &
      scratch_14 + scratch_17 + scratch_18 + scratch_20 + scratch_22 + &
      scratch_24 + scratch_27 + scratch_3 &
       )

    ydot_nuc(jo16) = ( &
      scratch_14 + scratch_24 - scratch_25 - scratch_7 &
       )

    ydot_nuc(jo20) = ( &
      scratch_28 - scratch_29 &
       )

    ydot_nuc(jf20) = ( &
      -scratch_28 + scratch_29 + scratch_30 - scratch_31 &
       )

    ydot_nuc(jne20) = ( &
      -scratch_14 + scratch_22 + scratch_23 - scratch_30 + scratch_31 &
       )

    ydot_nuc(jmg24) = ( &
      scratch_18 + scratch_20 + scratch_21 + scratch_3 &
       )

    ydot_nuc(jal27) = ( &
      scratch_17 + scratch_5 &
       )

    ydot_nuc(jsi28) = ( &
      scratch_19 + scratch_27 + scratch_4 &
       )

    ydot_nuc(jp31) = ( &
      scratch_13 + scratch_16 &
       )

    ydot_nuc(js32) = ( &
      scratch_12 + scratch_26 &
       )


  end subroutine rhs_nuc

  
  subroutine actual_jac(state)

    !$acc routine seq

    use burn_type_module, only: net_itemp, net_ienuc
    
    implicit none
    
    type(burn_t) :: state
    type(rate_eval_t) :: rate_eval
    type(plasma_state) :: pstate
    double precision :: reactvec(num_rate_groups+2)
    double precision :: screened_rates_dt(nrates)
    double precision :: dfdy_nuc(nspec, nspec)
    double precision :: Y(nspec)
    double precision :: dens, temp, ye, rhoy, b1
    double precision :: sneut, dsneutdt, dsneutdd, snuda, snudz
    integer :: i, j

    dens = state%rho
    temp = state%T

    ! Set molar abundances
    Y(:) = state%xn(:) * aion_inv(:)
    
    call evaluate_rates(state, rate_eval)
    
    ! Species Jacobian elements with respect to other species
    call jac_nuc(dfdy_nuc, Y, rate_eval % screened_rates, dens)
    state%jac(1:nspec, 1:nspec) = dfdy_nuc

    ! Species Jacobian elements with respect to energy generation rate
    state%jac(1:nspec, net_ienuc) = 0.0d0

    ! Evaluate the species Jacobian elements with respect to temperature by
    ! calling the RHS using the temperature derivative of the screened rate
    screened_rates_dt = rate_eval % unscreened_rates(i_rate, :) * &
         rate_eval % unscreened_rates(i_dscor_dt, :) + &
         rate_eval % unscreened_rates(i_drate_dt, :) * &
         rate_eval % unscreened_rates(i_scor, :)

    call rhs_nuc(state%jac(1:nspec, net_itemp), Y, screened_rates_dt, dens)
    
    ! Energy generation rate Jacobian elements with respect to species
    do j = 1, nspec
       call ener_gener_rate(state % jac(1:nspec,j), state % jac(net_ienuc,j))
    enddo

    ! Account for the thermal neutrino losses
    call sneut5(temp, dens, state%abar, state%zbar, sneut, dsneutdt, dsneutdd, snuda, snudz)
    do j = 1, nspec
       b1 = ((aion(j) - state%abar) * state%abar * snuda + (zion(j) - state%zbar) * state%abar * snudz)
       state % jac(net_ienuc,j) = state % jac(net_ienuc,j) - b1
    enddo

    ! Energy generation rate Jacobian element with respect to energy generation rate
    state%jac(net_ienuc, net_ienuc) = 0.0d0

    ! Energy generation rate Jacobian element with respect to temperature
    call ener_gener_rate(state%jac(1:nspec, net_itemp), state%jac(net_ienuc, net_itemp))
    state%jac(net_ienuc, net_itemp) = state%jac(net_ienuc, net_itemp) - dsneutdt

    ! Add dqweak and epart contributions!!!

    ! Temperature Jacobian elements
    call temperature_jac(state)

  end subroutine actual_jac

  subroutine jac_nuc(dfdy_nuc, Y, screened_rates, dens)

    !$acc routine seq
    

    double precision, intent(out) :: dfdy_nuc(nspec, nspec)
    double precision, intent(in)  :: Y(nspec)
    double precision, intent(in)  :: screened_rates(nrates)
    double precision, intent(in)  :: dens

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

    scratch_0 = Y(jp31)*dens
    scratch_1 = screened_rates(k_p_p31__he4_si28)*scratch_0
    scratch_2 = screened_rates(k_p_p31__s32)*scratch_0
    scratch_3 = -scratch_1 - scratch_2
    scratch_4 = Y(jal27)*dens
    scratch_5 = screened_rates(k_p_al27__he4_mg24)*scratch_4
    scratch_6 = screened_rates(k_p_al27__si28)*scratch_4
    scratch_7 = -scratch_5 - scratch_6
    scratch_8 = screened_rates(k_he4_mg24__p_al27)*dens
    scratch_9 = Y(jmg24)*scratch_8
    scratch_10 = screened_rates(k_he4_si28__p_p31)*dens
    scratch_11 = Y(jsi28)*scratch_10
    scratch_12 = screened_rates(k_o16_o16__p_p31)*Y(jo16)*dens
    scratch_13 = 1.0d0*scratch_12
    scratch_14 = Y(jhe4)*scratch_8
    scratch_15 = Y(jp)*dens
    scratch_16 = screened_rates(k_p_al27__he4_mg24)*scratch_15
    scratch_17 = screened_rates(k_p_al27__si28)*scratch_15
    scratch_18 = -scratch_16 - scratch_17
    scratch_19 = Y(jhe4)*scratch_10
    scratch_20 = screened_rates(k_p_p31__he4_si28)*scratch_15
    scratch_21 = screened_rates(k_p_p31__s32)*scratch_15
    scratch_22 = -scratch_20 - scratch_21
    scratch_23 = screened_rates(k_he4_al27__p31)*dens
    scratch_24 = Y(jal27)*scratch_23
    scratch_25 = -scratch_24
    scratch_26 = -scratch_9
    scratch_27 = screened_rates(k_he4_mg24__si28)*dens
    scratch_28 = Y(jmg24)*scratch_27
    scratch_29 = -scratch_28
    scratch_30 = screened_rates(k_he4_ne20__mg24)*dens
    scratch_31 = Y(jne20)*scratch_30
    scratch_32 = -scratch_31
    scratch_33 = screened_rates(k_he4_o16__ne20)*dens
    scratch_34 = Y(jo16)*scratch_33
    scratch_35 = -scratch_34
    scratch_36 = screened_rates(k_he4_si28__s32)*dens
    scratch_37 = Y(jsi28)*scratch_36
    scratch_38 = -scratch_11 - scratch_37
    scratch_39 = Y(jhe4)*scratch_33
    scratch_40 = -scratch_39
    scratch_41 = screened_rates(k_o16_o16__he4_si28)*Y(jo16)*dens
    scratch_42 = 1.0d0*scratch_41
    scratch_43 = Y(jhe4)*scratch_30
    scratch_44 = -scratch_43
    scratch_45 = Y(jhe4)*scratch_27
    scratch_46 = -scratch_14 - scratch_45
    scratch_47 = Y(jhe4)*scratch_23
    scratch_48 = -scratch_47
    scratch_49 = Y(jhe4)*scratch_36
    scratch_50 = -scratch_19 - scratch_49

    dfdy_nuc(jp,jp) = ( &
      scratch_3 + scratch_7 &
       )

    dfdy_nuc(jp,jhe4) = ( &
      scratch_11 + scratch_9 &
       )

    dfdy_nuc(jp,jo16) = ( &
      scratch_13 &
       )

    dfdy_nuc(jp,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp,jne20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp,jmg24) = ( &
      scratch_14 &
       )

    dfdy_nuc(jp,jal27) = ( &
      scratch_18 &
       )

    dfdy_nuc(jp,jsi28) = ( &
      scratch_19 &
       )

    dfdy_nuc(jp,jp31) = ( &
      scratch_22 &
       )

    dfdy_nuc(jp,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jhe4,jp) = ( &
      scratch_1 + scratch_5 &
       )

    dfdy_nuc(jhe4,jhe4) = ( &
      scratch_25 + scratch_26 + scratch_29 + scratch_32 + scratch_35 + &
      scratch_38 &
       )

    dfdy_nuc(jhe4,jo16) = ( &
      scratch_40 + scratch_42 &
       )

    dfdy_nuc(jhe4,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jhe4,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jhe4,jne20) = ( &
      screened_rates(k_ne20__he4_o16) + scratch_44 &
       )

    dfdy_nuc(jhe4,jmg24) = ( &
      scratch_46 &
       )

    dfdy_nuc(jhe4,jal27) = ( &
      scratch_16 + scratch_48 &
       )

    dfdy_nuc(jhe4,jsi28) = ( &
      scratch_50 &
       )

    dfdy_nuc(jhe4,jp31) = ( &
      scratch_20 &
       )

    dfdy_nuc(jhe4,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jp) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jhe4) = ( &
      scratch_35 &
       )

    dfdy_nuc(jo16,jo16) = ( &
      -2.0d0*scratch_12 + scratch_40 - 2.0d0*scratch_41 &
       )

    dfdy_nuc(jo16,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jne20) = ( &
      screened_rates(k_ne20__he4_o16) &
       )

    dfdy_nuc(jo16,jmg24) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jal27) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jsi28) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,jp31) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo16,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jp) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jhe4) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jo16) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jo20) = ( &
      -screened_rates(k_o20__f20) &
       )

    dfdy_nuc(jo20,jf20) = ( &
      screened_rates(k_f20__o20) &
       )

    dfdy_nuc(jo20,jne20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jmg24) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jal27) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jsi28) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,jp31) = ( &
      0.0d0 &
       )

    dfdy_nuc(jo20,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jp) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jhe4) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jo16) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jo20) = ( &
      screened_rates(k_o20__f20) &
       )

    dfdy_nuc(jf20,jf20) = ( &
      -screened_rates(k_f20__ne20) - screened_rates(k_f20__o20) &
       )

    dfdy_nuc(jf20,jne20) = ( &
      screened_rates(k_ne20__f20) &
       )

    dfdy_nuc(jf20,jmg24) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jal27) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jsi28) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,jp31) = ( &
      0.0d0 &
       )

    dfdy_nuc(jf20,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,jp) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,jhe4) = ( &
      scratch_32 + scratch_34 &
       )

    dfdy_nuc(jne20,jo16) = ( &
      scratch_39 &
       )

    dfdy_nuc(jne20,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,jf20) = ( &
      screened_rates(k_f20__ne20) &
       )

    dfdy_nuc(jne20,jne20) = ( &
      -screened_rates(k_ne20__f20) - screened_rates(k_ne20__he4_o16) + scratch_44 &
       )

    dfdy_nuc(jne20,jmg24) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,jal27) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,jsi28) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,jp31) = ( &
      0.0d0 &
       )

    dfdy_nuc(jne20,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jmg24,jp) = ( &
      scratch_5 &
       )

    dfdy_nuc(jmg24,jhe4) = ( &
      scratch_26 + scratch_29 + scratch_31 &
       )

    dfdy_nuc(jmg24,jo16) = ( &
      0.0d0 &
       )

    dfdy_nuc(jmg24,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jmg24,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jmg24,jne20) = ( &
      scratch_43 &
       )

    dfdy_nuc(jmg24,jmg24) = ( &
      scratch_46 &
       )

    dfdy_nuc(jmg24,jal27) = ( &
      scratch_16 &
       )

    dfdy_nuc(jmg24,jsi28) = ( &
      0.0d0 &
       )

    dfdy_nuc(jmg24,jp31) = ( &
      0.0d0 &
       )

    dfdy_nuc(jmg24,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,jp) = ( &
      scratch_7 &
       )

    dfdy_nuc(jal27,jhe4) = ( &
      scratch_25 + scratch_9 &
       )

    dfdy_nuc(jal27,jo16) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,jne20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,jmg24) = ( &
      scratch_14 &
       )

    dfdy_nuc(jal27,jal27) = ( &
      scratch_18 + scratch_48 &
       )

    dfdy_nuc(jal27,jsi28) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,jp31) = ( &
      0.0d0 &
       )

    dfdy_nuc(jal27,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jsi28,jp) = ( &
      scratch_1 + scratch_6 &
       )

    dfdy_nuc(jsi28,jhe4) = ( &
      scratch_28 + scratch_38 &
       )

    dfdy_nuc(jsi28,jo16) = ( &
      scratch_42 &
       )

    dfdy_nuc(jsi28,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jsi28,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jsi28,jne20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jsi28,jmg24) = ( &
      scratch_45 &
       )

    dfdy_nuc(jsi28,jal27) = ( &
      scratch_17 &
       )

    dfdy_nuc(jsi28,jsi28) = ( &
      scratch_50 &
       )

    dfdy_nuc(jsi28,jp31) = ( &
      scratch_20 &
       )

    dfdy_nuc(jsi28,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp31,jp) = ( &
      scratch_3 &
       )

    dfdy_nuc(jp31,jhe4) = ( &
      scratch_11 + scratch_24 &
       )

    dfdy_nuc(jp31,jo16) = ( &
      scratch_13 &
       )

    dfdy_nuc(jp31,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp31,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp31,jne20) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp31,jmg24) = ( &
      0.0d0 &
       )

    dfdy_nuc(jp31,jal27) = ( &
      scratch_47 &
       )

    dfdy_nuc(jp31,jsi28) = ( &
      scratch_19 &
       )

    dfdy_nuc(jp31,jp31) = ( &
      scratch_22 &
       )

    dfdy_nuc(jp31,js32) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jp) = ( &
      scratch_2 &
       )

    dfdy_nuc(js32,jhe4) = ( &
      scratch_37 &
       )

    dfdy_nuc(js32,jo16) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jo20) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jf20) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jne20) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jmg24) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jal27) = ( &
      0.0d0 &
       )

    dfdy_nuc(js32,jsi28) = ( &
      scratch_49 &
       )

    dfdy_nuc(js32,jp31) = ( &
      scratch_21 &
       )

    dfdy_nuc(js32,js32) = ( &
      0.0d0 &
       )

    
  end subroutine jac_nuc

end module actual_rhs_module
