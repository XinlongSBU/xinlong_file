# 1 "/raid2/xinlong/git_folder/Microphysics/unit_test/eos_override.F90"
# 1 "<built-in>"
# 1 "<命令行>"

# 1 "/usr/include/stdc-predef.h" 1 3 4

# 17 "/usr/include/stdc-predef.h" 3 4























# 1 "<命令行>" 2
# 1 "/raid2/xinlong/git_folder/Microphysics/unit_test/eos_override.F90"
module eos_override_module

  implicit none

  public eos_override

contains

  ! This is a user hook to override the details of the EOS state.

  subroutine eos_override(state)

    use eos_type_module, only: eos_t

    implicit none

    type (eos_t) :: state

    !$gpu

  end subroutine eos_override

end module eos_override_module
