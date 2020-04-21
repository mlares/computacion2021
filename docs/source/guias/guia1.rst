Ayuda para la guia 1
====================


Ejercicio 1.7
-------------

----
        
Un esferoide oblato como la Tierra es obtenido rotando una elipse sobre su
eje menor. La superficie del esferoide esta dada por la siguiente fórmula:

.. math::

      A(r1, r2) = 2 \pi r^2_1 \left[1 + \frac{1 − e^2}{e} atanh(e)\right],

en donde :math:`r_1` es el semieje ecuatorial y :math:`r_2` es el semieje polar,
   con :math:`r_1 > r_2`, y e es la excentricidad dada por 

.. math::

      e = \sqrt{1-\left(\frac{r_2}{r_1}\right)^2},

Escriba un programa que tenga como valores de entrada :math:`r_1` y :math:`r_2` y
   muestre los valores de :math:`A(r1, r2)` y su aproximación:
   
.. math::

      A(r1, r2) \simeq 4\pi \left( \frac{1}{2} (r_1 + r_2) \right)^2.

Aplique al programa los datos de la Tierra :math:`(r_1, r_2) = (6378.137, 6356.752)\,km` y encuentre en qué dígito se encuentra la discrepancia. 
   
----

Para resolver este ejercicio vamos a hacer un script de python y
correrlo como está explicado en la sección :ref:`usage`.

Veamos primero cómo hacer los cálculos.  Debemos calcular dos
valores de la superficie de un esferoide.  Un valor es exacto y el
otro es aproximado.

Para el valor exacto:

.. math::

    A(r1, r2) = 2 \pi r^2_1 \left[1 + \frac{1 − e^2}{e} atanh(e)\right],
 

debemos usar dos cosas que no están disponibles en python al menos que
se "llamen" ciertas herramientas: el número :math:`pi` y las funciones
:math:`arctan` y :math:`sqrt`.

Ambas están en el paquete math.  Para que estén disponibles, debemos
cargarlas explícitamente:

.. code:: python

   from math import pi, arctan, sqrt

Como ejercicio, se puede probar usar pi y las funciones antes y
despues de cargarlas desde el módulo math.


Recordemos que siempre podemos acceder a la :ref:`help` de python para saber
más sobre una función o un objeto cualquiera.

Recordar que hay varias formas de cargar herramientas usando módulos,
ir a la sección :ref:`modules` para más información.


Ahora podemos escribir la fórmula exacta y la aproximada:

.. code:: python

    r1 = 6378.137
    r2 = 6356.752
    e = sqrt(1 - (r2/r1)**2)   
    A_exacta = 2*pi * r1**2 * (1-e**2)*e * arctan(e)
    A_aprox = 4*pi*(*(r1 + r2))**2


Eso es todo!  Ahora vamos a tratar de hacer esto más amigable para un
usuario del programa.  Las cosas que podríamos hacer son:

- que pregunte los valores de los radios
- que muestre en pantalla los valores del área
- que guarde en un archivo los valores del área
- que lea de un archivo los valores de los radios
- que grafique la diferencia entre la formula exacta y la aproximada
  en función del valor de e





