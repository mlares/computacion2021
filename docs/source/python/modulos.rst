.. ayuda sobre modulos

****************
Módulos
****************


Los módulos permiten organizar la forma de escribir código, contribuyendo a:

Simplicidad:
   Los modulos resuelven problemas simples y cortos, y se pueden
   usar luego en proyectos más complejos.

Mantenibilidad:
   Permiten limitar cada módulo a un tipo de problemas.

Reusabilidad:
   Un módulo se puede usar en muchos proyectos.

Contexto:
   Permite evitar conflictos con otras partes del programa por los 
   nombres de las variables.



Para cargar los objetos de un módulo se pueden usar varias estrategias.  Por ejemplo, para cargar el módulo pyplot, se puede hacer:

.. code:: python

   from matplotlib import pyplot as plt
   import matplotlib.pyplot



.. code:: python

   import math
   mypi = math.pi

   from math import pi
   mypi = pi

   from math import *
   mypi = pi

   import math as m
   mypi = m.pi






