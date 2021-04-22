"""
roots_tools

Módulo con funciones para resolver ecuaciones de una variable
"""

def biseccion_recursiva(f, a, b, ftol, xtol, Niter):
    """
    Calcula la raíz de una función por el método de biseccion.

    Parameters
    ----------
    f: function

    a: float

    b: float

    ftol: float

    xtol: float

    Niter: int

    Returns
    -------
    x: float
       aproximación de la raíz de la función


    """
    a=Inter[0]; b=Inter[1]
    fa=f(a)
    dist=(b-a)/2
    x=a+dist
    if dist<xtol:
        print('distancia a solución alcanzada')
        return x
    fx=f(x)
    if abs(fx)<ftol:
        print('valor funcional menor a tolerancia')
        return x
    if Niter==0:
        print('máximo de iteraciones alcanzado')
        return x

    if fx*fa<0:
        return rbiseccion(f,[a,x],ftol,xtol,Niter-1)
    else:
        return rbiseccion(f,[x,b],ftol,xtol,Niter-1) 


def biseccion_iterativa(f,Inter,ftol,xtol,Niter):
    """
    biseccion
    """

