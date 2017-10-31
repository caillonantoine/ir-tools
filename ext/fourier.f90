subroutine dft(x,y,N)
    implicit none
    integer, intent(in) :: N
    complex, intent(in), dimension(N) :: x
    complex, intent(out), dimension(N) :: y

    complex, dimension(N) :: temp
    real :: pi,theta
    integer :: i,j

    pi = 3.14159265359

    do i=1,N
    	do j=1,N
    		theta = -2*pi*i*j/N
    		temp(j) = x(j)*complex(cos(theta),sin(theta))
    	enddo
    	y(i) = sum(temp)
    enddo

end subroutine dft

subroutine idft(x,y,N)
    implicit none
    integer, intent(in) :: N
    complex, intent(in), dimension(N) :: x
    complex, intent(out), dimension(N) :: y

    complex, dimension(N) :: temp
    real :: pi,theta
    integer :: i,j

    pi = 3.14159265359

    do i=1,N
    	do j=1,N
    		theta = 2*pi*i*j/N
    		temp(j) = x(j)*complex(cos(theta),sin(theta))
    	enddo
    	y(i) = sum(temp)
    enddo

end subroutine idft

recursive subroutine ifft(x,y,N)
    implicit none
    integer, intent(in) :: N
    complex, intent(in), dimension(N) :: x
    complex, intent(out), dimension(N) :: y

    complex, dimension(N/2) :: xeven,xodd
    real :: pi,theta
    integer :: i

    pi = 3.14159265359

    if (N < 16) then
    	call dft(x,y,N)
    else
    	call fft(x(1:N:2),xeven,N/2)
    	call fft(x(2:N:2),xodd,N/2)
    	do i=1,N/2
    		theta = -2*pi*i/N
    		y(i) = xeven(i) + complex(cos(theta),sin(theta))*xodd(i)
    		theta = -2*pi*(i + N/2)/N
    		y(i + N/2) = xeven(i) + complex(cos(theta),sin(theta))*xodd(i)
    	enddo
    endif

    
end subroutine ifft

recursive subroutine fft(x,y,N)
    implicit none
    integer, intent(in) :: N
    complex, intent(in), dimension(N) :: x
    complex, intent(out), dimension(N) :: y

    complex, dimension(N/2) :: xeven,xodd
    real :: pi,theta
    integer :: i

    pi = 3.14159265359

    if (N < 16) then
    	call dft(x,y,N)
    else
    	call fft(x(1:N:2),xeven,N/2)
    	call fft(x(2:N:2),xodd,N/2)
    	do i=1,N/2
    		theta = 2*pi*i/N
    		y(i) = xeven(i) + complex(cos(theta),sin(theta))*xodd(i)
    		theta = 2*pi*(i + N/2)/N
    		y(i + N/2) = xeven(i) + complex(cos(theta),sin(theta))*xodd(i)
    	enddo
    endif

    
end subroutine fft