










module debug_module


  implicit none

  private

contains

  subroutine print_mf(lev, lo, hi, mf, m_lo, m_hi, nc_m) bind (C,name="print_mf")
    
    integer         , intent (in   ) :: lev, lo(3), hi(3)
    integer         , intent (in   ) :: m_lo(3), m_hi(3), nc_m
    double precision, intent (inout) :: mf(m_lo(1):m_hi(1),m_lo(2):m_hi(2),m_lo(3):m_hi(3),nc_m)

    integer comp,i,j,k

    print*,"level",lev
    print*,"valid box",lo(1:3),hi(1:3)

    ! loop over the data
    do comp = 1, nc_m
    do k = m_lo(3),m_hi(3)
    do j = m_lo(2),m_hi(2)
    do i = m_lo(1),m_hi(1)
       print*,'lev,i,j,k,comp',lev,i,j,k,comp,mf(i,j,k,comp)
    enddo
    enddo
    enddo
    enddo

    call flush(6)

  end subroutine print_mf

  subroutine print_edge(lev, lo, hi, mf, m_lo, m_hi, nc_m) bind (C,name="print_edge")
    
    integer         , intent (in   ) :: lev, lo(3), hi(3)
    integer         , intent (in   ) :: m_lo(3), m_hi(3), nc_m
    double precision, intent (inout) :: mf(m_lo(1):m_hi(1),m_lo(2):m_hi(2),m_lo(3):m_hi(3),nc_m)

    integer comp,i,j,k

    print*,"level",lev
    print*,"valid box",lo(1:3),hi(1:3)

    ! loop over the data
    do comp = 1, nc_m
    do k = m_lo(3),m_hi(3)
    do j = m_lo(2),m_hi(2)
    do i = m_lo(1),m_hi(1)
       print*,'lev,i,j,k,comp',lev,i,j,k,comp,mf(i,j,k,comp)
    enddo
    enddo
    enddo
    enddo

    call flush(6)

  end subroutine print_edge

end module debug_module
