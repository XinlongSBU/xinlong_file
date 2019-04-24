! Module actual_burner_module defined in file tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90

subroutine f90wrap_actual_burner_init
    use actual_burner_module, only: actual_burner_init
    implicit none
    
    call actual_burner_init()
end subroutine f90wrap_actual_burner_init

subroutine f90wrap_actual_burner_finalize
    use actual_burner_module, only: actual_burner_finalize
    implicit none
    
    call actual_burner_finalize()
end subroutine f90wrap_actual_burner_finalize

subroutine f90wrap_actual_burner(state_in, state_out, dt, time)
    use burn_type_module, only: burn_t
    use actual_burner_module, only: actual_burner
    implicit none
    
    type burn_t_ptr_type
        type(burn_t), pointer :: p => NULL()
    end type burn_t_ptr_type
    type(burn_t_ptr_type) :: state_in_ptr
    integer, intent(in), dimension(2) :: state_in
    type(burn_t_ptr_type) :: state_out_ptr
    integer, intent(in), dimension(2) :: state_out
    real(8) :: dt
    real(8) :: time
    state_in_ptr = transfer(state_in, state_in_ptr)
    state_out_ptr = transfer(state_out, state_out_ptr)
    call actual_burner(state_in=state_in_ptr%p, state_out=state_out_ptr%p, dt=dt, &
        time=time)
end subroutine f90wrap_actual_burner

! End of module actual_burner_module defined in file tmp_build_dir/f/3d.gnu.EXE/F90PP-actual_burner.F90

