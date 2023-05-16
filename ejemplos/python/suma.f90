program suma

implicit none
real :: a
real :: b
real :: c

write(*,*) 'Ingrese el valor a: '
read(*,*) a
write(*,*) 'Ingrese el valor b: '
read(*,*) b

c = a + b

write(*,*) 'La suma es: ', c

end program suma
