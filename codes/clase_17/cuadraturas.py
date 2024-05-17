def contar_argumentos(func):
    def inner(*args, **kwargs):
        nargs_in = len(args) + len(kwargs)
        return func(*args, **kwargs, nargs_in=nargs_in)
    return inner

# REGLAS SIMPLES

# con funciones

def cuad_pmedio_funcion(a, b, f):
    """Implementación de la regla del punto medio
    
    Parameters
    ----------
    f: La función a integrar
    a: Límite inferior del intervalo
    b: Límite superior del intervalo
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    """
    if a > b:
        raise ValueError("Oops!  Debe ser a<b")
        return None
    try:
        x0 = (a+b)/2
        h = f(x0)
        aprox = h*(b-a)
    except:
        print('Error: no fue posible calcular la función')
    return aprox

def cuad_trapecio_funcion(a, b, f):
    """Implementación de la regla del trapecio
    
    Parameters
    ----------
    f: La función a integrar
    a: Límite inferior del intervalo
    b: Límite superior del intervalo
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del trapecio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    """
    if a > b:
        raise ValueError("Oops!  Debe ser a<b")
        return None
    try:
        h = f(a) + f(b)
        aprox = (b-a)/2*h
    except:
        print('Error: no fue posible calcular la función')
    return aprox

def cuad_simpson_funcion(a, b, f):
    """Implementación de la regla de Simpson
    
    Parameters
    ----------
    f: La función a integrar
    a: Límite inferior del intervalo
    b: Límite superior del intervalo
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla de Simpson
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    """
    if a > b:
        raise ValueError("Oops!  Debe ser a<b")
        return None
    try:
        x0 = (a+b)/2
        h = f(a) + f(b) + 4*f(x0)
        aprox = (b-a)/6*h
    except:
        print('Error: no fue posible calcular la función')
    return aprox


# con datos

def cuad_pmedio_datos(a, b, y0):
    """Implementación de la regla del punto medio
    
    Parameters
    ----------
    f: La función a integrar
    a: Límite inferior del intervalo
    b: Límite superior del intervalo
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    """
    try:
        x0 = (a+b)/2
        aprox = x0*y0
    except:
        print('Error: no fue posible calcular la función')
    return aprox

def cuad_pmedio_datos(a, b, f=None, y0=None):
    """Implementación de la regla del punto medio
    
    Parameters
    ----------
    a: float
       Límite inferior del intervalo
    b: float
       Límite superior del intervalo
    f: function (1 parameter)
       La función a integrar
    y0: float
       El valor de y en el punto medio.
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    """
    if a > b:
        raise ValueError("Oops!  Debe ser a<b")

    x0 = (a+b)/2
    if (f is None) and (y0 is not None):
            aprox = x0*y0
    elif (f is not None) and (y0 is None):            
        try:
            h = f(x0)
        except:
            print(('Error: no fue posible calcular la función'
                   ' Si desea ingresar un dato use y0='))
        aprox = h*(b-a)

    else:
        raise ValueError("Debe ingresar la función o los datos!")            
            
    return aprox

def cuad_trapecio_datos(x0, x1, f=None, y0=None, y1=None):
    """Implementación de la regla del trapecio
    
    Parameters
    ----------
    x0: float
       Límite inferior del intervalo
    x1: float
       Límite superior del intervalo
    f: function (1 parameter)
       La función a integrar
    y0: float
       El valor de y en el punto medio.
    y1: float
       El valor de y en el punto medio.

    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        cuad_trapecio(x0, x1, f=f)
        cuad_trapecio(x0, x1, y0=f(x0), y1=f(x1))
    """
    if x0 > x1:
        raise ValueError("Oops!  Debe ser a<b")

    if (f is None) and (y0 is not None) and (y1 is not None):
            aprox = (x1-x0)*(y0+y1)/2
    elif (f is not None) and (y0 is None):            
        try:
            y0 = f(x0)
            y1 = f(x1)
        except:
            print(('Error: no fue posible calcular la función'
                   ' Si desea ingresar un dato use y0='))
        aprox = (x1-x0)*(y0+y1)/2

    else:
        raise ValueError("Debe ingresar la función o los datos!")            
            
    return aprox


# con funciones o datos
 
def cuad_pmedio(x0, x1, f=None, y0=None, nargs_in=None):
    """Implementación de la regla del punto medio
    
    Parameters
    ----------
    x0: float
       Límite inferior del intervalo
    x1: float
       Límite superior del intervalo
    f: function (1 parameter)
       La función a integrar
    y0: float
       El valor de y en el punto medio.
    y1: float
       El valor de y en el punto medio.

    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        cuad_trapecio(x0, x1, f=f)
        cuad_trapecio(x0, x1, y0=f(x0), y1=f(x1))
    """
    if nargs_in==4:
        y1=y0        
        y0=f
        f = None
    elif nargs_in==3:
        if type(f) is float:        
            raise ValueError("Verificar los argumentos")
    else:
        raise ValueError("Verificar el número de argumentos")



            
    if x0 > x1:
        raise ValueError("Oops!  Debe ser a<b")




    if (f is None) and (y0 is not None):
            aprox = (x1-x0)*y0
    elif (f is not None) and (y0 is None):            
        try:
            y0 = f(x0)
        except:
            print(('Error: no fue posible calcular la función'
                   ' Si desea ingresar un dato use y0='))
        aprox = (x1-x0)*y0

    else:
        raise ValueError("Debe ingresar la función o los datos!")            
            
    return aprox

@contar_argumentos
def cuad_trapecio(x0, x1, f=None, y0=None, y1=None, nargs_in=None):
    """Implementación de la regla del trapecio
    
    Parameters
    ----------
    x0: float
       Límite inferior del intervalo
    x1: float
       Límite superior del intervalo
    f: function (1 parameter)
       La función a integrar
    y0: float
       El valor de y en el punto medio.
    y1: float
       El valor de y en el punto medio.

    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        cuad_trapecio(x0, x1, f=f)
        cuad_trapecio(x0, x1, y0=f(x0), y1=f(x1))
    """
    if nargs_in==4:
        y1=y0        
        y0=f
        f = None
    elif nargs_in==3:
        if type(f) is float:        
            raise ValueError("Verificar los argumentos")
    else:
        raise ValueError("Verificar el número de argumentos")
            
    if x0 > x1:
        raise ValueError("Oops!  Debe ser a<b")

    if (f is None) and (y0 is not None) and (y1 is not None):
            aprox = (x1-x0)*(y0+y1)/2
    elif (f is not None) and (y0 is None):            
        try:
            y0 = f(x0)
            y1 = f(x1)
        except:
            print(('Error: no fue posible calcular la función'
                   ' Si desea ingresar un dato use y0='))
        aprox = (x1-x0)*(y0+y1)/2

    else:
        raise ValueError("Debe ingresar la función o los datos!")            
            
    return aprox

@contar_argumentos
def cuad_simpson_datos(x0, x2, f=None, y0=None, y1=None, y2=None, 
                       nargs_in=None):
    """Implementación de la regla de simpson
    
    Parameters
    ----------
    x0: float
       Límite inferior del intervalo
    x2: float
       Límite superior del intervalo
    f: function (1 parameter)
       La función a integrar
    y0: float
       El valor de y en el punto medio.
    y2: float
       El valor de y en el punto medio.
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla de Simpson
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        cuad_simpson(x0, x2, f=f)
        cuad_simpson(x0, x2, y0=f(x0), y2=f(x2))
        cuad_simpson(x0, x2, f)
        cuad_simpson(x0, x2, y0, y2)
    """
    
    if nargs_in==5:
        y2=y1
        y1=y0
        y0=f
        f = None
    elif nargs_in==3:
        if type(f) is float:        
            raise ValueError("Verificar los argumentos")
    else:
        raise ValueError("Verificar el número de argumentos")
            
    if x0 > x2:
        raise ValueError("Oops!  Debe ser a<b")
        
    x1 = (x0+x2)/2

    if (f is None) and (y0 is not None) and (y1 is not None):
            aprox = (x2-x0)/6 * (y0 + 4*y1 + y2)
    elif (f is not None) and (y0 is None):            
        try:
            y0 = f(x0)
            y1 = f(x1)
            y2 = f(x2)
        except:
            print(('Error: no fue posible calcular la función'
                   ' Si desea ingresar un dato use y0='))
        aprox = (x2-x0)/6 * (y0 + 4*y1 + y2)

    else:
        raise ValueError("Debe ingresar la función o los datos!")            
            
    return aprox


# REGLAS COMPUESTAS

# PUNTO MEDIO

def punto_medio_compuesta(x, f=None, y=None):
    """Implementación de la regla del punto medio compuesta
    
    Parameters
    ----------
    x: list or array
       Lista de valores de x
    f: function (1 parameter)
       La función a integrar
    y: list or array
       La lista de valores de y en los puntos medios
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del punto medio compuesta
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        punto_medio_compuesta(x, f=f)
    """
    import numpy as np

    # Primero verificar si la particion es regular    
    x = np.array(x)
    x.sort()    
    H = (max(x) - min(x)) / (len(x) - 1)
    equiesp = np.std(np.diff(x)) < H * 1.e-6
    
    if not equiesp:
        raise ValueError("La partición no es regular.")

    # Calcular los valores de y en los puntos medios (si se pasó una función)
    if (y is None) and (f is not None):
        mid_points = (x[:-1] + x[1:]) / 2
        y = f(mid_points)
        
    # Si no se pasa la función f, se debe proporcionar y
    if y is None:
        raise ValueError("Debe proporcionar una función o una lista de valores de y.")
    
    # Calcular la integral por la regla del punto medio compuesta
    aprox = H * np.sum(y)
    
    return aprox

# TRAPECIO

def trapecio_compuesta(x, f=None, y=None):
    """Implementación de la regla del trapecio compuesta
    
    Parameters
    ----------
    x: list or array
       Lista de valores de x
    f: function (1 parameter)
       La función a integrar
    y: list or array
       La lista de valores de y
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla del trapecio compuesta
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        trapecio_compuesta(x, f=f)
    """
    import numpy as np

    # Primero verificar si la partición es regular    
    x = np.array(x)
    x.sort()    
    H = (max(x) - min(x)) / (len(x) - 1)
    equiesp = np.std(np.diff(x)) < H * 1.e-6
    
    if not equiesp:
        raise ValueError("La partición no es regular.")
    
    # Calcular los valores de y (si se pasó una función)
    if (y is None) and (f is not None):
        y = f(x)
        
    # Si no se pasa la función f, se debe proporcionar y
    if y is None:
        raise ValueError("Debe proporcionar una función o una lista de valores de y.")
    
    # Calcular la integral por la regla del trapecio compuesta
    n = len(x)
    aprox = (y[0] + y[-1] + 2 * np.sum(y[1:-1])) * (H / 2)
    
    return aprox




# SIMPSON

def cuad_simpson_compuesta(x, f=None, y=None):
    """Implementación de la regla de simpson
    
    Parameters
    ----------
    x: list or array
       Lista de valores de x
    f: function (1 parameter)
       La función a integrar
    y: list or array
       La lista de valores de y
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla de Simpson
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        cuad_simpson(x, y=y)
        cuad_simpson(x, f=f)
    """
    import numpy as np

    # Primero verificar si la particion es regular    
    x = np.array(x)
    x.sort()    
    H = (max(x) - min(x))/len(x-1)
    equiesp = np.std(np.diff(x)) < H*1.e-6
    
    # Calcular los valores de y (si se pasó una función)
    if (y is None) and (f is not None):
        y = f(x)
        
    n = len(x)
    
    if equiesp:        
        impares = y[1:-1:2].sum()
        pares = y[2:-1:2].sum()        
        H = y[0] + 2*pares + 4*impares + y[-1] 
        H = H / (3*n)
        aprox = (x[-1]-x[0])*H
    else:
        aprox = 0
        for i in range(0, len(x)-2, 2):
            aprox += cuad_simpson(x[i], x[i+2], y[i], y[i+1], y[i+2])
            
    return aprox

def cuad_simpson_compuesta_II(f, I, eps, apply_correc=False):
    """Implementación de la regla de Simpson
    
    Parameters
    ----------
    I: list
       Intervalo de integración, ingresado como lista de dos elementos
    f: function (1 parameter)
       La función a integrar
    eps: tolerancia
    
    Returns
    -------
    aprox: Aproximación de la integral por la regla de Simpson
    
    Notes
    -----
    Este código es parte del curso "Computación", Famaf
    Uso:  
        cuad_simpson_compuesta_II(f, I)
        cuad_simpson_compuesta_II(f, I)
    """
    import numpy as np

    delta = 2*eps
    n = 2
    aprox_old = (I[1]-I[0])*f((I[1]+I[0])/2)

    while delta > eps:
        x = np.linspace(I[0], I[1], n)
        aprox = cuad_simpson_compuesta(x, f=f)
        delta = abs(aprox - aprox_old)
        if apply_correc:
            delta = delta/15
        aprox_old = aprox
        n += 1
        if n>5000:
            break

    return aprox
