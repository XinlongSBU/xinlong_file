module reaclib_rates
  use screening_module, only: screen5, add_screening_factor, screening_init, plasma_state, fill_plasma_state
  use network

  implicit none

  logical, parameter :: screen_reaclib = .true.
  
  ! Temperature coefficient arrays (numbers correspond to reaction numbers in net_info)
  double precision, allocatable :: ctemp_rate(:,:)

  ! Index into ctemp_rate, dimension 2, where each rate's coefficients start
  integer, allocatable :: rate_start_idx(:)
  
  ! Reaction multiplicities-1 (how many rates contribute - 1)
  integer, allocatable :: rate_extra_mult(:)

  ! Should these reactions be screened?
  logical, allocatable :: do_screening(:)
  
  !$acc declare create(ctemp_rate, rate_start_idx, rate_extra_mult, do_screening)
  !$acc declare copyin(screen_reaclib)

contains

  subroutine init_reaclib()
    
    allocate( ctemp_rate(7, 36) )
    ! o20__f20
    ctemp_rate(:, 1) = [  &
        -2.96920000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00 ]

    ! f20__ne20
    ctemp_rate(:, 2) = [  &
        -2.77346000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00 ]

    ! ne20__he4_o16
    ctemp_rate(:, 3) = [  &
        3.42658000000000d+01, &
        -6.76518000000000d+01, &
        0.00000000000000d+00, &
        -3.65925000000000d+00, &
        7.14224000000000d-01, &
        -1.07508000000000d-03, &
        0.00000000000000d+00 ]

    ctemp_rate(:, 4) = [  &
        2.86431000000000d+01, &
        -6.52460000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00 ]

    ctemp_rate(:, 5) = [  &
        4.86604000000000d+01, &
        -5.48875000000000d+01, &
        -3.97262000000000d+01, &
        -2.10799000000000d-01, &
        4.42879000000000d-01, &
        -7.97753000000000d-02, &
        8.33333000000000d-01 ]

    ! he4_o16__ne20
    ctemp_rate(:, 6) = [  &
        3.88571000000000d+00, &
        -1.03585000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 7) = [  &
        2.39030000000000d+01, &
        0.00000000000000d+00, &
        -3.97262000000000d+01, &
        -2.10799000000000d-01, &
        4.42879000000000d-01, &
        -7.97753000000000d-02, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 8) = [  &
        9.50848000000000d+00, &
        -1.27643000000000d+01, &
        0.00000000000000d+00, &
        -3.65925000000000d+00, &
        7.14224000000000d-01, &
        -1.07508000000000d-03, &
        -1.50000000000000d+00 ]

    ! he4_ne20__mg24
    ctemp_rate(:, 9) = [  &
        -8.79827000000000d+00, &
        -1.27809000000000d+01, &
        0.00000000000000d+00, &
        1.69229000000000d+01, &
        -2.57325000000000d+00, &
        2.08997000000000d-01, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 10) = [  &
        1.98307000000000d+00, &
        -9.22026000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 11) = [  &
        -3.87055000000000d+01, &
        -2.50605000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 12) = [  &
        2.45058000000000d+01, &
        0.00000000000000d+00, &
        -4.62525000000000d+01, &
        5.58901000000000d+00, &
        7.61843000000000d+00, &
        -3.68300000000000d+00, &
        -6.66667000000000d-01 ]

    ! he4_mg24__si28
    ctemp_rate(:, 13) = [  &
        -5.05494000000000d+01, &
        -1.28332000000000d+01, &
        2.13721000000000d+01, &
        3.77649000000000d+01, &
        -4.10635000000000d+00, &
        2.49618000000000d-01, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 14) = [  &
        8.03977000000000d+00, &
        -1.56290000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ! p_al27__si28
    ctemp_rate(:, 15) = [  &
        8.60234000000000d+01, &
        -3.87313000000000d-01, &
        -2.68327000000000d+01, &
        -1.16137000000000d+02, &
        9.50567000000000d-03, &
        9.99755000000000d-03, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 16) = [  &
        2.11065000000000d+01, &
        0.00000000000000d+00, &
        -2.32205000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -2.00000000000000d+00, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 17) = [  &
        -1.36664000000000d+01, &
        -1.90396000000000d+00, &
        0.00000000000000d+00, &
        2.38634000000000d+01, &
        -3.70135000000000d+00, &
        2.89640000000000d-01, &
        -1.50000000000000d+00 ]

    ! he4_al27__p31
    ctemp_rate(:, 18) = [  &
        4.72333000000000d+01, &
        0.00000000000000d+00, &
        -5.65351000000000d+01, &
        -8.96208000000000d-01, &
        -1.72024000000000d+00, &
        1.85409000000000d-01, &
        -6.66667000000000d-01 ]

    ! he4_si28__s32
    ctemp_rate(:, 19) = [  &
        4.79212000000000d+01, &
        0.00000000000000d+00, &
        -5.94896000000000d+01, &
        4.47205000000000d+00, &
        -4.78989000000000d+00, &
        5.57201000000000d-01, &
        -6.66667000000000d-01 ]

    ! p_p31__s32
    ctemp_rate(:, 20) = [  &
        1.92596000000000d+01, &
        0.00000000000000d+00, &
        -2.53278000000000d+01, &
        6.49310000000000d+00, &
        -9.27513000000000d+00, &
        -6.10439000000000d-01, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 21) = [  &
        8.21556000000000d-01, &
        -3.77704000000000d+00, &
        0.00000000000000d+00, &
        8.09341000000000d+00, &
        -6.15971000000000d-01, &
        3.11590000000000d-02, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 22) = [  &
        -2.66839000000000d+00, &
        -2.25958000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ! o16_o16__p_p31
    ctemp_rate(:, 23) = [  &
        8.52628000000000d+01, &
        2.23453000000000d-01, &
        -1.45844000000000d+02, &
        8.72612000000000d+00, &
        -5.54035000000000d-01, &
        -1.37562000000000d-01, &
        -6.88807000000000d+00 ]

    ! o16_o16__he4_si28
    ctemp_rate(:, 24) = [  &
        9.72435000000000d+01, &
        -2.68514000000000d-01, &
        -1.19324000000000d+02, &
        -3.22497000000000d+01, &
        1.46214000000000d+00, &
        -2.00893000000000d-01, &
        1.32148000000000d+01 ]

    ! he4_mg24__p_al27
    ctemp_rate(:, 25) = [  &
        3.00397000000000d+01, &
        -1.85791000000000d+01, &
        -2.64162000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -2.00000000000000d+00, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 26) = [  &
        -2.62862000000000d+01, &
        -1.95422000000000d+01, &
        5.18642000000000d+00, &
        -3.47936000000000d+01, &
        1.68225000000000d+02, &
        -1.15825000000000d+02, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 27) = [  &
        -6.44575000000000d+00, &
        -2.28216000000000d+01, &
        0.00000000000000d+00, &
        1.80416000000000d+01, &
        -1.54137000000000d+00, &
        8.47506000000000d-02, &
        -1.50000000000000d+00 ]

    ! p_al27__he4_mg24
    ctemp_rate(:, 28) = [  &
        -2.68683000000000d+01, &
        -9.63012000000000d-01, &
        5.18642000000000d+00, &
        -3.47936000000000d+01, &
        1.68225000000000d+02, &
        -1.15825000000000d+02, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 29) = [  &
        2.94576000000000d+01, &
        0.00000000000000d+00, &
        -2.64162000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -2.00000000000000d+00, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 30) = [  &
        -7.02789000000000d+00, &
        -4.24250000000000d+00, &
        0.00000000000000d+00, &
        1.80416000000000d+01, &
        -1.54137000000000d+00, &
        8.47506000000000d-02, &
        -1.50000000000000d+00 ]

    ! he4_si28__p_p31
    ctemp_rate(:, 31) = [  &
        6.03424000000000d+01, &
        -2.22348000000000d+01, &
        -3.19320000000000d+01, &
        -7.70334000000000d+01, &
        -4.36847000000000d+01, &
        -4.28955000000000d+00, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 32) = [  &
        -1.34595000000000d+01, &
        -2.41120000000000d+01, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 33) = [  &
        -1.14335000000000d+01, &
        -2.56606000000000d+01, &
        0.00000000000000d+00, &
        2.15210000000000d+01, &
        -1.90355000000000d+00, &
        9.27240000000000d-02, &
        -1.50000000000000d+00 ]

    ! p_p31__he4_si28
    ctemp_rate(:, 34) = [  &
        -1.29190000000000d+01, &
        -1.87716000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        0.00000000000000d+00, &
        -1.50000000000000d+00 ]

    ctemp_rate(:, 35) = [  &
        6.08829000000000d+01, &
        0.00000000000000d+00, &
        -3.19320000000000d+01, &
        -7.70334000000000d+01, &
        -4.36847000000000d+01, &
        -4.28955000000000d+00, &
        -6.66667000000000d-01 ]

    ctemp_rate(:, 36) = [  &
        -1.08930000000000d+01, &
        -3.42575000000000d+00, &
        0.00000000000000d+00, &
        2.15210000000000d+01, &
        -1.90355000000000d+00, &
        9.27240000000000d-02, &
        -1.50000000000000d+00 ]



    allocate( rate_start_idx(nrat_reaclib) )
    rate_start_idx(:) = [ &
      1, &
      2, &
      3, &
      6, &
      9, &
      13, &
      15, &
      18, &
      19, &
      20, &
      23, &
      24, &
      25, &
      28, &
      31, &
      34 ]

    allocate( rate_extra_mult(nrat_reaclib) )
    rate_extra_mult(:) = [ &
      0, &
      0, &
      2, &
      2, &
      3, &
      1, &
      2, &
      0, &
      0, &
      2, &
      0, &
      0, &
      2, &
      2, &
      2, &
      2 ]

    allocate( do_screening(nrat_reaclib) )
    do_screening(:) = [ &
      .false., &
      .false., &
      .false., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true., &
      .true. ]

    !$acc update device(ctemp_rate, rate_start_idx, rate_extra_mult, do_screening)
    
  end subroutine init_reaclib

  subroutine term_reaclib()
    deallocate( ctemp_rate )
    deallocate( rate_start_idx )
    deallocate( rate_extra_mult )
    deallocate( do_screening )
  end subroutine term_reaclib

  subroutine net_screening_init()
    ! Adds screening factors and calls screening_init

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jo16), aion(jo16))

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jne20), aion(jne20))

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jmg24), aion(jmg24))

    call add_screening_factor(zion(jp), aion(jp), &
      zion(jal27), aion(jal27))

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jal27), aion(jal27))

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jsi28), aion(jsi28))

    call add_screening_factor(zion(jp), aion(jp), &
      zion(jp31), aion(jp31))

    call add_screening_factor(zion(jo16), aion(jo16), &
      zion(jo16), aion(jo16))

    call add_screening_factor(zion(jo16), aion(jo16), &
      zion(jo16), aion(jo16))

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jmg24), aion(jmg24))

    call add_screening_factor(zion(jp), aion(jp), &
      zion(jal27), aion(jal27))

    call add_screening_factor(zion(jhe4), aion(jhe4), &
      zion(jsi28), aion(jsi28))

    call add_screening_factor(zion(jp), aion(jp), &
      zion(jp31), aion(jp31))


    call screening_init()    
  end subroutine net_screening_init

  subroutine reaclib_evaluate(pstate, temp, iwhich, reactvec)
    !$acc routine seq

    implicit none
    
    type(plasma_state), intent(in) :: pstate
    double precision, intent(in) :: temp
    integer, intent(in) :: iwhich

    double precision, intent(inout) :: reactvec(num_rate_groups+2)
    ! reactvec(1) = rate     , the reaction rate
    ! reactvec(2) = drate_dt , the Temperature derivative of rate
    ! reactvec(3) = scor     , the screening factor
    ! reactvec(4) = dscor_dt , the Temperature derivative of scor
    ! reactvec(5) = dqweak   , the weak reaction dq-value (ergs)
    !                          (This accounts for modification of the reaction Q
    !                           due to the local density and temperature of the plasma.
    !                           For Reaclib rates, this is 0.0d0.)
    ! reactvec(6) = epart    , the particle energy generation rate (ergs/s)
    ! NOTE: The particle energy generation rate (returned in ergs/s)
    !       is the contribution to enuc from non-ion particles associated
    !       with the reaction.
    !       For example, this accounts for neutrino energy losses
    !       in weak reactions and/or gamma heating of the plasma
    !       from nuclear transitions in daughter nuclei.

    double precision  :: rate, scor ! Rate and Screening Factor
    double precision  :: drate_dt, dscor_dt ! Temperature derivatives
    double precision :: dscor_dd
    double precision :: ri, T9, T9_exp, lnirate, irate, dirate_dt, dlnirate_dt
    integer :: i, j, m, istart

    ri = 0.0d0
    rate = 0.0d0
    drate_dt = 0.0d0
    irate = 0.0d0
    dirate_dt = 0.0d0
    T9 = temp/1.0d9
    T9_exp = 0.0d0
    scor = 1.0d0
    dscor_dt = 0.0d0
    dscor_dd = 0.0d0

    ! Use reaction multiplicities to tell whether the rate is Reaclib
    m = rate_extra_mult(iwhich)

    istart = rate_start_idx(iwhich)

    do i = 0, m
       lnirate = ctemp_rate(1, istart+i) + ctemp_rate(7, istart+i) * LOG(T9)
       dlnirate_dt = ctemp_rate(7, istart+i)/T9
       do j = 2, 6
          T9_exp = (2.0d0*dble(j-1)-5.0d0)/3.0d0 
          lnirate = lnirate + ctemp_rate(j, istart+i) * T9**T9_exp
          dlnirate_dt = dlnirate_dt + &
               T9_exp * ctemp_rate(j, istart+i) * T9**(T9_exp-1.0d0)
       end do
       ! If the rate will be in the approx. interval [0.0, 1.0E-100], replace by 0.0
       ! This avoids issues with passing very large negative values to EXP
       ! and getting results between 0.0 and 1.0E-308, the limit for IEEE 754.
       ! And avoids SIGFPE in CVODE due to tiny rates.
       lnirate = max(lnirate, -230.0d0)
       irate = EXP(lnirate)
       rate = rate + irate
       dirate_dt = irate * dlnirate_dt/1.0d9
       drate_dt = drate_dt + dirate_dt
    end do

    if ( screen_reaclib .and. do_screening(iwhich) ) then
       call screen5(pstate, iwhich, scor, dscor_dt, dscor_dd)
    end if

    reactvec(i_rate)     = rate
    reactvec(i_drate_dt) = drate_dt
    reactvec(i_scor)     = scor
    reactvec(i_dscor_dt) = dscor_dt
    reactvec(i_dqweak)   = 0.0d0
    reactvec(i_epart)    = 0.0d0

    ! write(*,*) '----------------------------------------'
    ! write(*,*) 'IWHICH: ', iwhich
    ! write(*,*) 'reactvec(i_rate)', reactvec(i_rate)
    ! write(*,*) 'reactvec(i_drate_dt)', reactvec(i_drate_dt)
    ! write(*,*) 'reactvec(i_scor)', reactvec(i_scor)    
    ! write(*,*) 'reactvec(i_dscor_dt)', reactvec(i_dscor_dt)
    ! write(*,*) 'reactvec(i_dqweak)', reactvec(i_dqweak)
    ! write(*,*) 'reactvec(i_epart)', reactvec(i_epart)
    ! write(*,*) '----------------------------------------'

  end subroutine reaclib_evaluate
  
end module reaclib_rates
