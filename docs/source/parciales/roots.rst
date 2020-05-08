***********************************
Ejercicios del parcial 1
***********************************

En esta sección vemos algunos ejemplos de ejercicios de raíces.

Consideremos la función dada por:

.. math::

   f(x) = cos(x) - x


Primero definimos y visualizamos la función:

.. code:: python

   def f(x):
       # una funcion
       import numpy as np
       return(x-np.cos(x))

   def df(x):
       return(1+np.sin(x))

   x = np.linspace(start=-3.15, stop=3.15, num=150)

   plt.close('all')
   fig = plt.figure(figsize=(10, 6))
   ax = fig.add_subplot()
   ax.set_title('x - cos(x)', fontsize=18)
   ax.plot(x, f(x))
   plt.show()


Bisección
=================

.. https://www.geogebra.org/m/mNY3NPuU

Busquemos las raices con el metodo de la bisección:

.. code:: python

   def bisec(f, a, b, Ex, Ef, N):
       # implementacion de la funcion de biseccion

       # 1. verificar que f(a)*f(b) < 0
       if f(a)*f(b) >= 0:
           print('no se puede aplicar este metodo')
           return None
       cond = True
       n = 0
       c_ant = (a+b)/2
       xn = []
       errx = []
       errf = []
       fxn = []
       while cond:
           c = (a+b)/2
           if f(a)*f(c) < 0:
               b = c
           elif f(c)*f(b) < 0:
               a = c
           else:
               print('no se puede')

           n += 1
           cond = n<N and (abs(f(c))>Ef or abs(c-c_ant)>Ex)
           xn.append(c)
           fxn.append(f(c))
           errx.append(abs(c-c_ant))
           errf.append(abs(f(c)))
           c_ant = c
       return ((xn, fxn, errx, errf))


Para usar la función:     

.. code:: python


   a = 0
   b = 2
   Ex = 1.e-6
   Ef = 1.e-7
   N = 100
   xn, fxn, errx, errf = bisec(f, a, b, Ex, Ef, N)



Newton
=================

Recordemos la idea del método:
 
.. raw:: html

    <embed>

 <iframe scrolling="no" src="https://www.geogebra.org/material/iframe/id/29635304/width/800/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/true/ld/false/sri/false" width="800px" height="600px" style="border:0px;" allowfullscreen> </iframe>

    </embed>

 


Busquemos las raices con el metodo de Newton:
 

.. code:: python


   def newton(f, df, x0, Ex, Ef, N):

       # 1. verificar que df(x0)!=0
       if df(x0) < 1.e-10:
           print('no se puede')
           return None

       cond = True
       n = 0
       xn = [x0]
       x = x0
       errx = []
       errf = []
       fxn = []
       while cond:

           x_ant = x
           x = x - f(x)/df(x)

           n += 1
           cond = n<N and (abs(f(x))>Ef or abs(x - x_ant)>Ex)

           xn.append(x)
           fxn.append(f(x))
           errx.append(abs(x-x_ant))
           errf.append(abs(f(x)))

       return ((xn, fxn, errx, errf))


Para usar la función:
     
.. code:: python

   x0 = 1.
   Ex = 1.e-6
   Ef = 1.e-7
   N = 100
   xn, fxn, errx, errf = newton(f, df, x0, Ex, Ef, N)   

Secante
=================



Busquemos las raices con el metodo de la secante:

.. code:: python


   def secante(f, x1, x2, Ex, Ef, N):

       cond = True
       n = 0
       xn = []
       errx = []
       errf = []
       fxn = []
       while cond:

           x = x2 - f(x2)*(x2-x1)/(f(x2)-f(x1))

           n += 1
           cond = n<N and (abs(f(x))>Ef or abs(x - x2)>Ex)
           x1 = x2
           x2 = x

           xn.append(x)
           fxn.append(f(x))
           errx.append(abs(x-x2))
           errf.append(abs(f(x)))

       return ((xn, fxn, errx, errf))   
    
Para usar la función:
     
.. code:: python

   x1 = -0.5
   x2 = 0.5
   Ex = 1.e-6
   Ef = 1.e-7
   N = 100
   xn, fxn, errx, errf = secante(f, x1, x2, Ex, Ef, N)   
                    
Punto fijo
=================

.. raw:: html

    <embed>

 <iframe scrolling="no" src="https://www.geogebra.org/material/iframe/id/29653854/width/800/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/true/ld/false/sri/false" width="800px" height="600px" style="border:0px;" allowfullscreen> </iframe>

    </embed>
 

Busquemos las raices con el metodo del punto fijo: 

.. code:: python



   def puntofijo(f, g, x0, Ex, Ef, N):

       cond = True
       n = 0
       xn = []
       x = x0
       errx = []
       errf = []
       fxn = []
       while cond:

           x_ant = x
           x = g(x)

           n += 1
           cond = n<N and (abs(f(x))>Ef or abs(x - x_ant)>Ex)

           xn.append(x)
           fxn.append(f(x))
           errx.append(abs(x-x_ant))
           errf.append(abs(f(x)))

       return ((xn, fxn, errx, errf))                        
    
   def g1(x):
       return(np.cos(x))

   def g2(x):
       return(np.arccos(x))         

Para usar la función:
     
.. code:: python

   x0 = 2
   Ex = 1.e-6
   Ef = 1.e-7
   N = 100

   xn, fxn, errx, errf = puntofijo(f, g1, x0, Ex, Ef, N)   


También podemos graficar las distintas aproximaciones en la iteración:

.. code:: python

                    
   plt.close('all')
   fig = plt.figure(figsize=(8, 4))
   ax = fig.subplots(2, 1)
   x = np.linspace(-1, 1, 100)
   ax[0].plot(x, g1(x), x, x)
   ax[1].plot(x, g2(x), x, x)
   plt.show()                            



.. https://www.geogebra.org/m/Q2yMukrD
