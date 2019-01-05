










module burner_module

  use bl_types
  use bl_constants_module
  use network
  use eos_module
  use actual_burner_module
  use burn_type_module

  logical :: burner_initialized = .false.

contains

  subroutine burner_init() bind(C, name="burner_init")

    implicit none

    call actual_burner_init()

    burner_initialized = .true.

  end subroutine burner_init



  subroutine burner(state_in, state_out, dt)

    !$acc routine seq

    implicit none

    type (burn_t), intent(inout) :: state_in
    type (burn_t), intent(inout) :: state_out
    double precision, intent(in) :: dt

    double precision :: time

    time = 0.d0

    ! Make sure the network and burner have been initialized.

    if (.NOT. network_initialized) then
       call bl_error("ERROR in burner: must initialize network first.")
    endif

    if (.NOT. burner_initialized) then
       call bl_error("ERROR in burner: must initialize burner first.")
    endif

    ! Initialize the final state by assuming it does not change.

    state_out = state_in

    ! Do the burning.

    call actual_burner(state_in, state_out, dt, time)

  end subroutine burner

end module burner_module
