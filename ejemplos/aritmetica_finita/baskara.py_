import math as m
import numpy as np
from matplotlib import pyplot as plt

a=1; b=-62.1; c=1
x1=(-b+m.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-m.sqrt(b**2-4*a*c))/(2*a)
print('x1=',x1,', x2=',x2)
print('p(x1)=',a*x1**2+b*x1+c)
print('p(x2)=',a*x2**2+b*x2+c)

x = np.linspace(-2, 2, 1000)
y = a*x**2+b*x+c

plt.plot(x, y)



def raizCuad(a,b,c):
  D=b**2-4*a*c
  if D>0:
    if b>=0:
      x1=-2*c/(b+m.sqrt(D))
      x2=(-b-m.sqrt(D))/(2*a)
    else:
      x1=(-b-m.sqrt(D))/(2*a)
      x2=-2*c/(b-m.sqrt(D))
    return [x1,x2]
  elif D==0:
    x=-b/(2*a)
    return x
  else:
    return "no existen raíces reales"

a=1; b=62.1; c=1
xnuevo=raizCuad(a,b,c)
print(xnuevo)
print('p(x1)=',a*xnuevo[0]**2+b*xnuevo[0]+c)
print('p(x2)=',a*xnuevo[1]**2+b*xnuevo[1]+c)




