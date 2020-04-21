.. ayuda sobre plots en python

********************
Gráficos con python
********************

El lenguaje python permite realizar una amplia variedad de
visualizaciones de datos.  La misma se realiza mediante la ayuda
de módulos (como math o numpy) que están destinados a brindar
herramientas de visualización.  

En la lista que sigue se presentan algunos de los módulos más usados.
El objetivo no es aprenderlos, sino saber que existen varias opciones
y disminuir un poco la confusión que se puede producir al principio
al buscar ayuda y bibliografía:

* Matplotlib
* Seaborn
* Plotly
* Bokeh
* Altair
* Pygal
* Pandas

La elección de una de estas herramientas para hacer un gráfico depende del
contexto, para qué se quiere hacer el gráfico, dónde se va a mostrar y a partir
de qué datos.  Así, por ejemplo, Plotly, Bokeh y Altair devuelven gráficos en
HTML para ser mostrados en páginas web, Pygal genera gráficos vectoriales y
Pandas grafica datos guardados en cierto tipo especial de estructura.

En este tutorial (y en la materia) usaremos solamente Matplotlib.


El módulo Matplotlib
========================

Matplotlib es un módulo de python que ofrece una librería para graficar.

En general viene instalado con la distribución de python Anaconda, y si no se
puede instalar con el comando ``pip``:

.. code::

   pip install -U matplotlib

Una vez instalado, se puede acceder al módulo desde un entorno de python (es
decir, luego de "entrar" a python) con el comando import:

.. code:: python

   import matplotlib

aunque no es muy usual utilizarlo así.



Interface pyplot
========================

El módulo Matplotlib incluye una interface denominada ``pyplot`` que tiene todas las
herramientas para hacer gráficos sencillos.  Es posible que resulte un poco
confuso la utilización de términos como módulo, librería o interface, pero no es
necesario tener un conocimiento acabado de estos conceptos para producir
gráficos, ni está en el alcance de esta materia.  En este breve tutorial
aprenderemos lo básico para realizar gráficos aprendiendo a partir de ejemplos.

Para cargar esta interface, simplemente usamos el comando import:

.. code:: python

   import matplotlib.pyplot


Hay otras formas de hacer lo mismo, que se pueden encontrar en los numerosos
tutoriales que hay disponibles en internet.  Algunas de estas formas son:

.. code:: python

   from matplotlib import pyplot        #  (alternativa 1)
   from matplotlib import pyplot as plt #  (alternativa 2)
   import matplotlib.pyplot as plt      #  (alternativa 3)...

Esas tres líneas son equivalentes (sólo hay que usar una).  Notar que se
introdujo el alias ``plt``, que es una costumbre muy arraigada en la comunidad de
ciencias de datos.  Se puede reemplazar ``plt`` por cualquier otra cosa.  En lo
que sigue usaremos el alias ``plt`` como es usual.


Estilos de uso para pyplot
===========================

Antes de empezar a hacer gráficos, conviene aclarar que hay dos formas de usar
``Pyplot``.  Puede ser confuso leer la documentación disponible si no se tiene en
cuenta esto, ya que las mismas cosas sencillas se encuentran realizadas de
diferentes formas.  Esta sección está destinada a evitar esas confusiones al
mostrar las dos formas de trabajo, que son:

* estilo matlab
* estilo con orientación a objetos

Para el práctico se puede usar cualquiera de las dos.


Pyplot al estilo Matlab
-----------------------

Esta forma de usar Pyplot se llama "sintaxis imperativa", y fue diseñada
para parecerse a Matlab, que es otro lenguaje pensado para trabajar con matrices
que permite también hacer gráficos.

El gráfico de la función seno en Matlab se puede hacer así:

.. code:: matlab

   x = linspace(0,2*pi,100);
   y = sin(x);
   plot(x,y)
   xlabel('x')
   ylabel('sin(x)')
   title('Grafico de la funcion seno')

Ahora hacemos el mismo gráfico desde python:

.. code-block:: python
   :linenos:

   import numpy as np
   from matplotlib import pyplot as plt
   x = np.linspace(0, 2*np.pi, 100)
   y = np.sin(x)
   plt.plot(x, y)
   plt.xlabel('x')
   plt.ylabel('sin(x)')
   plt.title('Grafico de la funcion seno')
   plt.show()

En la línea 6 estamos creando un gráfico a partir de los arrays x e y, y a
partir de allí todo lo que hacemos con ``plt`` se aplica a ese gráfico.


Pyplot al estilo Orientación a Objetos
--------------------------------------

La orientación a objetos es un paradigma de programación (es decir, una forma de
programar justificada teóricamente) que permite estructurar el código utilizando
objetos que tienen propiedades o comportamientos.  Por ejemplo, un objeto de
tipo "animal" puede moverse de cierta forma, como caminar o nadar
(comportamiento) o tener cierta cantidad de patas (propiedad).  Un programa
puede tener varios objetos de tipo "animal" y no hace falta programar cada uno,
sino que basta con decir que "es un animal" y fácilmente adquiere la propiedad
de "número de patas" o el comportamiento de "forma de moverse".

Para hacer gráficos usando este concepto, trabajamos con dos objetos:

1. el objeto ``figure``, que es la figura y puede contener varios gráficos (o
   ``axes``)
2. el objeto ``axes``, que es la región que contiene un gráfico individual. No es
   lo mismo que los ejes (x/y axis).
 
En la siguiente figura (tomada de la documentacion de Matplotlib) se muestran
estos dos elementos, además de otros que usaremos para personalizar el aspecto
visual del gráfico.  Figure se refiere a toda la figura, y axes a la parte
interior del sistema de ejes.

.. image:: sphx_glr_anatomy_001.png
    :width: 600px
    :align: center
    :alt: Elementos de un gráfico   
       

Para generar una gráfico usando objetos, hay que crear un objeto de tipo ``figure``, y luego un objeto de tipo ``axes``, que es donde se realizará el gráfico.
 
.. code-block:: python
   :linenos:

   import numpy as np
   from matplotlib import pyplot as plt
   x = np.linspace(0, 2*np.pi, 100)
   y = np.sin(x)

   fig = plt.figure()
   fig.clf()
   ax = fig.add_subplot(1,1,1)
   ax.clear()
   ax.plot(x, y)
   ax.set_xlabel('x')
   ax.set_ylabel('sin(x)')
   ax.set_title('Grafico de la funcion seno')
   fig.show()                                                  
                      

aquí la función ``figure`` de pyplot crea una nueva figura, que está almacenada en
el objeto ``fig``.  Este objeto, que es de tipo figura, puede hacer ciertas cosas,
por ejemplo limpiar (``.clear()``) o mostrar (``.show()``) la figura.  Otra cosa que se puede hacer es crear un
objeto de tipo ``axes``, lo cual se hace en la línea 9 con la función
``add_subplot``.


Notar que add_subplot tiene 3 argumentos, para saber qué son podemos
acceder a la ayuda en la documentación, por ejemplo
desde el intérprete de ``ipython``, haciendo:
 
.. code::
             
   from matplotlib import pyplot as plt
   fig = plt.figure()
   fig.add_subplot?


Hay otras formas de usar los objetos ``figure`` y ``axes``, 
por ejemplo usando la función ``subplots`` de
Pyplot, que devuelve tanto la figura como los gráficos (``axes``) que contiene:

.. code-block:: python
   :linenos:

   import numpy as np
   from matplotlib import pyplot as plt
   x = np.linspace(0, 2*np.pi, 100)
   y = np.sin(x)

   fig, ax = plt.subplots()

   ax.plot(x, y)
   ax.set_xlabel('x')
   ax.set_ylabel('sin(x)')
   ax.set_title('Grafico de la funcion seno')
   fig.show()


Si quisiéramos hacer una figura con más de un gráfico, se usan los parámetros de
``add_subplot`` o de ``subplots`` (de nuevo, ver la ayuda).  Por ejemplo, para hacer los
gráficos de las funciones seno y coseno, uno al lado del otro:

.. code-block:: python
   :linenos:

   import numpy as np
   from matplotlib import pyplot as plt

   x = np.linspace(0, 2*np.pi, 100)
   y1 = np.sin(x)
   y2 = np.cos(x)

   fig, ax = plt.subplots(1, 2)

   ax[0].plot(x, y1)
   ax[0].set_xlabel('x')
   ax[0].set_ylabel('sin(x)')
   ax[0].set_title('Grafico de la funcion seno')

   ax[1].plot(x, y2)
   ax[1].set_xlabel('x')
   ax[1].set_ylabel('cos(x)')
   ax[1].set_title('Grafico de la funcion coseno')

   fig.show()               

Notar que ``subplots`` devuelve un objeto axes que es una lista, donde cada elemento
es un gráfico, es decir, ``ax[0]`` es el gráfico de la izquierda y ``ax[1]`` es el
gráfico de la derecha.  Al graficar, hay que decir en cuál de esos dos gráficos
estamos trabajando.

Para hacer los dos gráficos, pero uno arriba del otro, sólo hay que cambiar los
parámetros de ``plt.subplots`` (queda como ejercicio).




Obteniendo el gráfico
--------------------------------------

Dependiendo de la forma de trabajar, necesitaremos hacer distintas cosas para
obtener o visualizar el gráfico.

* Visualización en pantalla
* Utilizando Notebooks
* Salida a un archivo







Gráficos simples
========================

Ahora veremos ejemplos simples de cómo hacer gráficos en python usando
matplotlib. Existen varios tipos de gráficos que se pueden hacer, los
más simples son:


+----------------------+-------------------------------------+
| Tipo de gráfico      | ejemplo                             |
+======================+=====================================+
| lineas               | .. image:: line.png                 |
|                      |     :width: 300px                   |
|                      |     :align: center                  |
+----------------------+-------------------------------------+
| puntos (scatter)     | .. image:: scatter.png              |
|                      |     :width: 300px                   |
|                      |     :align: center                  |
+----------------------+-------------------------------------+
| barras               | .. image:: bars.png                 |
|                      |     :width: 300px                   |
|                      |     :align: center                  |
+----------------------+-------------------------------------+
| histograma           | .. image:: hist.png                 |
|                      |     :width: 300px                   |
|                      |     :align: center                  |
+----------------------+-------------------------------------+


Hay muchos otros, pero entendiendo estos pocos se puede fácilmente
incursionar en otros tipos de gráfico usando la documentación.


Varios gráficos en la misma figura
-----------------------------------

Para hacer varios gráficos en la misma figura se puede usar, como
vimos, las funciones ``subplots`` o ``add_subplot``.

.. code-block:: python

   from matplotlib import pyplot as plt
   x = np.linspace(-10, 10, 100)
   y1 = x
   y2 = x**2
   y3 = x**3
   y4 = x**4

   fig = plt.figure()
   fig.clf()
   ax = fig.subplots(2,2)

   ax[0,0].plot(x, y1)
   ax[0,0].set_xlabel('x')
   ax[0,0].set_ylabel('y')
   ax[0,0].set_title('y=x**1')

   ax[0,1].plot(x, y2)
   ax[0,1].set_xlabel('x')
   ax[0,1].set_ylabel('y')
   ax[0,1].set_title('y=x**2')

   ax[1,0].plot(x, y3)
   ax[1,0].set_xlabel('x')
   ax[1,0].set_ylabel('y')
   ax[1,0].set_title('y=x**3')
   
   ax[1,1].plot(x, y4)
   ax[1,1].set_xlabel('x')
   ax[1,1].set_ylabel('y')
   ax[1,1].set_title('y=x**4')
   
   fig.tight_layout()
   fig.show()        

Que da algo así:

.. image:: 4x4.png
    :width: 400px  
    :align: center

   

Varias lineas en el mismo grafico
-----------------------------------

Para graficar varias series de datos en el mismo gráfico 
se puede llamar a una función que grafique varias veces.
Por ejemplo, si queremos graficar las funciones seno y coseno en el
mismo gráfico, podemos proceder así:

.. code-block:: python

   from matplotlib import pyplot as plt
   x = np.linspace(-1, 1, 100)
   y1 = x
   y2 = x**2
   y3 = x**3
   y4 = x**4

   fig = plt.figure()
   fig.clf()
   ax = fig.subplots(1,1)

   ax.plot(x, y1, label='y=x**1')
   ax.plot(x, y2, label='y=x**2')
   ax.plot(x, y3, label='y=x**3')
   ax.plot(x, y4, label='y=x**4')
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   
   ax.legend()
   fig.tight_layout()
   fig.show()                
 

Que da algo así:

.. image:: 1x1.png
    :width: 400px  
    :align: center   


Atributos de los ejes
-----------------------------------

Se pueden modificar los atributos de los ejes, para lo cual primero
hay que identificar los diferentes elementos.  Las líneas de los ejes
que marcan los valores de la escala se llaman ``ticks``, cada tick
tiene una valor, que está dentro de un rango determinado.

Comencemos con el siguiente gráfico simple y tratemos de mejorarlo un
poco:

.. code-block:: python

   fig, ax = plt.subplots()
   N = 500
   x = np.random.rand(N)
   y = np.random.rand(N)
   plt.scatter(x, y)
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   plt.show()

.. image:: simple.png
    :width: 600px  
    :align: center 

.. code-block:: python

   fig, ax = plt.subplots()
   N = 500
   x = np.random.rand(N)
   y = np.random.rand(N)
   plt.scatter(x, y)
   ax.set_xlabel('x', fontsize=16)
   ax.set_ylabel('y', fontsize=16)

   ticks = [.2, .4, .6, .8]
   labels = ['0.2', '0.4', '0.6', '0.8']
   ax.set_xticks(ticks=ticks)
   ax.set_xticklabels(labels=labels, fontsize=16)
   ax.set_yticks(ticks=ticks)
   ax.set_yticklabels(labels=labels, fontsize=16)
   ax.tick_params(axis='x', direction='in', length=8, color='slategrey')
   ax.tick_params(axis='y', direction='in', length=8)
   plt.show()
  
  
.. image:: tunned.png
    :width: 600px  
    :align: center 

 


Atributos de las series de datos
-----------------------------------

Ahora tratemos de mejorar el contenido de los plots.  Hay muchos
atributos para trabajar, los más comunes son:

 
+------------------------+----------------------------+--------------------------------------------------+
|atributo                | modifica                   | opciones                                         |
+========================+============================+==================================================+
|alpha                   | transparencia              | escalar                                          |
+------------------------+----------------------------+--------------------------------------------------+
|color or c              | color                      | color de matplotlib                              |
+------------------------+----------------------------+--------------------------------------------------+
|label                   | etiqueta                   | cadena de carateres                              |
+------------------------+----------------------------+--------------------------------------------------+
|linestyle or ls         | tipo de linea              | ``[ '-' | '--' | '-.' | ':' | 'steps' | ...]``   |
+------------------------+----------------------------+--------------------------------------------------+
|linewidth or lw         | ancho de linea             | escalar                                          |
+------------------------+----------------------------+--------------------------------------------------+
|marker                  | marcador                   | ``[ '+' | ',' | '.' | '1' | '2' | '3' | '4' ]``  |
+------------------------+----------------------------+--------------------------------------------------+
|markeredgecolor or mec  | color de borde de marcador |color de  matplotlib                              |
+------------------------+----------------------------+--------------------------------------------------+
|markeredgewidth or mew  | grosor del marcador        | escalar                                          |
+------------------------+----------------------------+--------------------------------------------------+
|markerfacecolor or mfc  | color de relloeno marcador | color de matplotlib                              |
+------------------------+----------------------------+--------------------------------------------------+
|markersize or ms        | tamaño del marcador        | escalar                                          |
+------------------------+----------------------------+--------------------------------------------------+
|markevery               | un marcador cada...        | entero                                           |
+------------------------+----------------------------+--------------------------------------------------+



Entre los colores de Matplotlib, los más comunes se pueden usar con nombre:

.. image:: colors.png
    :width: 800px  
    :align: center 


Veamos ahora algunos gráficos donde hemos cambiado varios atributos.
La sintaxis es bastante simpĺe y es posible entender cómo funciona
leyendo el código:

.. code-block:: python

   fig, ax = plt.subplots()
   N = 500
   x = np.random.rand(N)
   y = np.random.rand(N)
   plt.scatter(x, y, s=44, color='cadetblue', alpha=0.6)
   ax.set_xlabel('x', fontsize=16)
   ax.set_ylabel('y', fontsize=16)

   ticks = [.2, .4, .6, .8]
   labels = ['0.2', '0.4', '0.6', '0.8']
   ax.set_xticks(ticks=ticks)
   ax.set_xticklabels(labels=labels, fontsize=16)
   ax.set_yticks(ticks=ticks)
   ax.set_yticklabels(labels=labels, fontsize=16)
   ax.tick_params(axis='x', direction='in', length=8, color='slategrey')
   ax.tick_params(axis='y', direction='in', length=8)
   plt.tight_layout()
   plt.show()          

.. image:: evenbetter.png
    :width: 800px  
    :align: center 
     

o con líneas:

.. code-block:: python

   from matplotlib import pyplot as plt
   x = np.linspace(-1, 1, 100)
   y1 = x
   y2 = x**2
   y3 = x**3
   y4 = x**4

   fig = plt.figure()
   fig.clf()
   ax = fig.subplots(1,1)

   ax.plot(x, y1, color='cornflowerblue', linewidth=2, label='y=x')
   ax.plot(x, y2, color='limegreen', linewidth=2, label='y=x^2')
   ax.plot(x, y3, color='tomato', linewidth=2, label='y=x^3')
   ax.plot(x, y4, color='darkorchid', linewidth=2, label='y=x^4')
           

   ticks = [(-1.0 + 0.5*i) for i in range(5)]
   labels = [f"{s: 2.1f}" for s in ticks]

   ax.set_xticks(ticks=ticks)
   ax.set_xticklabels(labels=labels, fontsize=16)
   ax.set_yticks(ticks=ticks)
   ax.set_yticklabels(labels=labels, fontsize=16)      
   ax.set_xlabel('x', fontsize=22)
   ax.set_ylabel('y', fontsize=22)
   ax.legend(loc='lower right', frameon=False,
             borderaxespad=4,
             ncol=2, handlelength=3)
   ax.xaxis.label.set_size(16)
   fig.tight_layout()
   fig.show()     



.. image:: evenbetter2.png
    :width: 800px  
    :align: center 
                     

.. `backends <https://matplotlib.org/3.2.1/tutorials/introductory/usage.html#backends>`._ 







