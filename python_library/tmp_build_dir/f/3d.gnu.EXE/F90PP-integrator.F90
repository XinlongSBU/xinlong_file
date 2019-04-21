












module integrator_module

  use amrex_error_module

  implicit none

  public

contains

  subroutine integrator_init()

    use integrator_scaling_module, only: integrator_scaling_init
    use actual_integrator_module, only: actual_integrator_init
    use temperature_integration_module, only: temperature_rhs_init

    implicit none

    call integrator_scaling_init()
    call actual_integrator_init()
    call temperature_rhs_init()

  end subroutine integrator_init



  subroutine integrator(state_in, state_out, dt, time)

    !$acc routine seq

    use actual_integrator_module, only: actual_integrator
    use amrex_fort_module, only : rt => amrex_real
    use amrex_constants_module, only: ZERO, ONE
    use burn_type_module, only: burn_t
    use integration_data, only: integration_status_t
    use extern_probin_module, only: rtol_spec, rtol_temp, rtol_enuc, &
                                    atol_spec, atol_temp, atol_enuc, &
                                    abort_on_failure, &
                                    retry_burn, retry_burn_factor, retry_burn_max_change

    implicit none

    type (burn_t),  intent(in   ) :: state_in
    type (burn_t),  intent(inout) :: state_out
    real(rt),     intent(in   ) :: dt, time

    !$gpu


    call actual_integrator(state_in, state_out, dt, time)


  end subroutine integrator

end module integrator_module
