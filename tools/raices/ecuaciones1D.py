class resultados_raiz:
    """
    clase para resultados de los métodos de búsqueda de raíces de
    ecuaciones escalares.
    """

    def __init__(self, x=None):
        # Inicialización del objeto
        self.x = x
        self.xlist = []
        self.convergencia = ''

    def __str__(self):
        # brinda la posibilidad de imprimir
        if self.x is None:
            ret = 'Aún no se ha calculado la raíz'
        else:
            ret = f'La aproximación de la raíz es {self.x}' 
        return ret
       


def biseccion(f, a, b,
              tolerancia_x=1.e-10, tolerancia_f=1.e-10, tolerancia_N=100,
              verbose=False, historico=False
             ):
    """
    Calcula una aproximación a una raíz de f por el método de bisección
    
    Parameters
    ----------
    f: function
    a: float
       limite inferior del intervalo
    b: float
       limite superior del intervalo       
    tolerrancia_x: float
       tolerancia para el error en x
    tolerrancia_f: float
       tolerancia para el error en f
    tolerrancia_N: int
       número máximo de iteraciones
    verbose: bool
       mostrar en pantalla los pasos de la iteración
    historico: bool
       devolver el histórico de todas las iteraciones

    El método para si (|f(x_k)|<tolerancia_f y |x_k-x_{k-1}|<tolerancia_x),
    o k=tolerancia_N
    
    returns
    -------
    r: resultados_raiz
       La aproximación de una raíz obtenida con el método y almacenada
       en un objeto de la clase resultados_raiz.

    Este código forma parte de las clases de la materia
    Computación, 2021, FaMAF
    """

    condición = True
    contador = 0
    x_anterior = a
    r = resultados_raiz()
    while condición:
        x = (a+b)/2
        if f(x)*f(a) > 0:
            a = x
        else:
            b = x
        if verbose:
            print(f'aproximación en el paso {contador}: x={x}')
        contador += 1
        cond1 = abs(x-x_anterior) > tolerancia_x
        cond2 = abs(f(x)-f(x_anterior)) > tolerancia_f
        cond3 = contador < tolerancia_N
        condición = (cond1 and cond2) or cond3
        x_anterior = x
        if historico:
            r.xlist.append(x)
        r.x = x

    return r

def newton(f, Df, x0,
           tolerancia_x=1.e-10, tolerancia_f=1.e-10, tolerancia_N=100,
           verbose=False, historico=False
          ):
    """
    Ejecuta el método de Newton para hallar una raíz de f.

    Parameters
    ----------
    f: function
       función a valores reales
    Df: function
       función derivada de f
    x0: float
       punto inicial

    tolerrancia_x: float
       tolerancia para el error en x
    tolerrancia_f: float
       tolerancia para el error en f
    tolerrancia_N: int
       número máximo de iteraciones
    verbose: bool
       mostrar en pantalla los pasos de la iteración
    historico: bool
       devolver el histórico de todas las iteraciones

    El método para si (|f(x_k)|<tolerancia_f y |x_k-x_{k-1}|<tolerancia_x),
    o k=tolerancia_N
 
    
    ftol: tolerancia de error en f
    xtol: tolerancia de error en x
    Niter: máximo de iteraciones permitidas    

    historico: True o False para retornar todas las iteraciones
    El método para si |f(x_k)|<ftol y |x_k-x_{k-1}|<xtol, o k=Niter

    returns
    -------
    r: resultados_raiz
       La aproximación de una raíz obtenida con el método y almacenada
       en un objeto de la clase resultados_raiz.

    Este código forma parte de las clases de la materia
    Computación, 2021, FaMAF
    """

    x = x0
    paradaX=True

    r = resultados_raiz()
    r.x = x

    for k in range(tolerancia_N + 1):
      fx = f(x)
      paradaF = (abs(fx) < tolerancia_f)
      Dfx = Df(x)
      paradaDF = (1 + abs(Dfx) > 1)
      if paradaF and paradaX:
        if verbose:
            print("La raíz es x=",x)
        return r
      if not paradaDF:
        if verbose:
            print("La derivada de la función es ",Dfx)
        return r
      d = -fx/Dfx
      paradaX=(abs(d) < tolerancia_x)
      x = x+d

      if historico:
          r.xlist.append(x)
      r.x = x

    if verbose:
        print("Máximo de iteraciones alcanzado")
    return r

def secante(f, x0, xaux,
            tolerancia_x=1.e-10, tolerancia_f=1.e-10, tolerancia_N=100,
            verbose=False, historico=False
           ):
    """Ejecuta el método secante para hallar una raíz de f, donde

    Parameters
    ----------
    f: función a valores reales
    x0: punto inicial
    xaux: punto inicial auxiliar distinto de x0

    verbose: bool
       mostrar en pantalla los pasos de la iteración
    historico: bool
       devolver el histórico de todas las iteraciones

    El método para si (|f(x_k)|<tolerancia_f y |x_k-x_{k-1}|<tolerancia_x),
    o k=tolerancia_N

    returns
    -------
    r: resultados_raiz
       La aproximación de una raíz obtenida con el método y almacenada
       en un objeto de la clase resultados_raiz.


    Este código forma parte de las clases de la materia
    Computación, 2021, FaMAF
    """
    x = x0
    r = resultados_raiz()
    r.x = x
    fx = f(x)
    faux = f(xaux)
    a = (fx-faux)/(x-xaux)
    paradaX=True
    for k in range(tolerancia_N):
      paradaF = (abs(fx) < tolerancia_f)
      if paradaF and paradaX:
          if verbose:
              print("La raíz es x=", x)
          return r
      d=-fx/a
      paradaDF=(1 + 1/abs(d) > 1)
      if not paradaDF:
          if verbose:
              print("La pendiente de la secante es ",a)
          return r
      paradaX=(abs(d) < tolerancia_x)
      x = x + d
      fxn = f(x)
      a = (fxn-fx)/d
      fx = fxn

      if historico:
          r.xlist.append(x)
      r.x = x

    return r

def puntofijo(g, x0,
              tolerancia_x=1.e-10, tolerancia_f=1.e-10, tolerancia_N=100,
              verbose=False, historico=False
              ):
    """Ejecuta el método de iteración de punto fijo para hallar un pf de g, donde

    Parameters
    ----------
    g: función a valores reales contractiva en un intervalo [a,b]
    x0: punto inicial en el intervalo [a,b]
    xtol: tolerancia de error en x
    Niter: máximo de iteraciones permitidas    
    historico: True o False para retornar todas las iteraciones
    El método para si |x_{k+1}-x_{k}|<xtol, o k=Niter

    returns
    -------
    r: resultados_raiz
       La aproximación de una raíz obtenida con el método y almacenada
       en un objeto de la clase resultados_raiz.


    Este código forma parte de las clases de la materia
    Computación, 2021, FaMAF
    """
    x = x0
    r = resultados_raiz()
    r.x = x
    for k in range(tolerancia_N):
      xn = g(r.x)
      if historico:
        r.xlist.append(xn)

      r.x = xn
      paradaX = (abs(xn-x) < tolerancia_x)
      if paradaX:
          if verbose:
              print("El punto fijo es x=",x)
          return r.xlist
      r.x = xn

    if verbose:
        print("Máximo de iteraciones alcanzado")

    return r



def aprox_raiz(f,
               df=None, g=None, intervalo=None, x0=None, xaux=None,
               metodo=None, **kwargs):
    """
    Función que combina diferentes métodos para calcular raíces

    Parameters
    ----------
    g: función a valores reales contractiva en un intervalo [a,b]
    x0: punto inicial en el intervalo [a,b]
    xtol: tolerancia de error en x
    Niter: máximo de iteraciones permitidas    
    historico: True o False para retornar todas las iteraciones
    El método para si |x_{k+1}-x_{k}|<xtol, o k=Niter

    returns
    -------
    r: resultados_raiz
       La aproximación de una raíz obtenida con el método y almacenada
       en un objeto de la clase resultados_raiz.


    Este código forma parte de las clases de la materia
    Computación, 2021, FaMAF
    """ 

    if metodo is None:
        print('Debe ingresar un método de la siguiente lista:')
        print('biseccion, newton, secante, puntofijo')
        return None

    metodo = metodo.lower().strip()

    metodo = ''.join(metodo.lower().split())

    if metodo in 'biseccion bisección bisection':
        if intervalo is None:
            print('Para el método de bisección debe ingresar un intervalo')
            return None
        else:
            a = intervalo[0]
            b = intervalo[1]
            r = biseccion(f, a, b, **kwargs)
    elif metodo in 'newton':
        if (df is None) or (x0 is None):
            msg = ('Para el método de Newton debe ingresar la derivada'
                   'y el valor inicial')
            print(msg)
            return None
        r = newton(f, df, x0, **kwargs)
    elif metodo in 'secante':
        if x0 is None:
            msg = ('Para el método de la secante debe ingresar '
                   'el valor inicial')
            print(msg)
        else:
            r = secante(f, x0, xaux, **kwargs)
    elif metodo in 'puntofijofixedpoint':
        if (g is None) or (x0 is None):
            msg = ('Para el método del punto fijo debe ingresar la'
                   'función g y x0')
            print(msg)
            return None
        else:
            r = puntofijo(g, x0, **kwargs)
    else:
        print('No se pudo reconocer el método')
        return None

    return r 

 
def aproxs_raiz(f, metodos=None, **kwargs):
    """
    Función que combina diferentes métodos para calcular raíces

    Parameters
    ----------
    g: función a valores reales contractiva en un intervalo [a,b]
    x0: punto inicial en el intervalo [a,b]
    xtol: tolerancia de error en x
    Niter: máximo de iteraciones permitidas    
    historico: True o False para retornar todas las iteraciones
    El método para si |x_{k+1}-x_{k}|<xtol, o k=Niter

    returns
    -------
    rs: list
       Las aproximaciones de una raíz obtenida con los métodos
       se devuelven en una lista de objetos de la clase resultados_raiz.

    Este código forma parte de las clases de la materia
    Computación, 2021, FaMAF
    """ 

    if metodos is None:
        print('Debe ingresar un método de la siguiente lista:')
        print('biseccion, newton, secante, puntofijo')
        return None

    rs = list()
    for metodo in metodos:
        r = aprox_raiz(f, metodo=metodo, **kwargs)
        rs.append(r)

    return rs
