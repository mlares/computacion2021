.. https://docutils.sourceforge.io/docs/user/rst/quickref.html


*******************************
Interactuando con python
*******************************

.. _usage:

Cómo correr un script de python
===============================

Hay muchas formas de correr los scripts de python.
En lo que sigue vamos a usar el simbolo $ para el prompt
de linux y el símbolo >>> para el prompt de python.

La primera forma es correr las sentencias de manera interactiva.  Para
ello, entrar a python y escribir:

.. code-block::

   x = 1
   y = 2
   print(x+y)


Para practicar las distintas formas de correr esto desde un archivo, 
vamos a escribir un script muy simple, y 
guardarlo en un archivo que se llame simple.py:

.. code-block:: python

   # contenidos del script simple.py
   x = 1
   y = 2
   print(x+y)

Para ejecutarlo se puede hacer desde una terminal:

.. code-block:: python

   python simple.py

Otras opciones son:

.. code-block:: python

    # python3
    exec(open('simple.py').read())

    # python2
    execfile('simple.py')

    # ipython3
    load simple.py
    run simple.py

