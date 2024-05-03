# Funciones para el ejercicio 4

from numpy import exp, log, cos, sin, sqrt
from numpy import empty, NAN, ndarray, zeros, append, float64

def pos(f, shift=0):
    def wrapper(x):
        if (type(x) is int) or (type(x) is float) or (type(x) is float64):
            if x > 0:
                z = f(x)
            else:
                z = NAN
        elif type(x) is list:
            z = []
            for ix in x:
                if ix > 0:
                    iz = f(ix)
                else:
                    iz = NAN
                z.append(iz)
        elif type(x) is ndarray:
            z = []
            for ix in x:
                if ix > 0:
                    iz = f(ix)
                else:
                    iz = NAN
                z.append(iz)
            # this version does not support unordered x-values
            #dominio = x>=0
            #x_pos = x[dominio]
            #z_pos = f(x_pos)
            #z_neg = zeros(sum(~dominio))
            #z_neg[:] = NAN
            #z = append(z_neg, z_pos)
        else:
            print("Error en el tipo de variable ingresada")
            return
        return z
    return wrapper
 

def threshold(shift=0):
    def inner(f):
        def wrapper(x):
            if (type(x) is int) or (type(x) is float) or (type(x) is float64):
                if x > shift:
                    z = f(x)
                else:
                    z = NAN
            elif type(x) is list:
                z = []
                for ix in x:
                    if ix > shift:
                        iz = f(ix)
                    else:
                        iz = NAN
                    z.append(iz)
            elif type(x) is ndarray:
                z = []
                for ix in x:
                    if ix > shift:
                        iz = f(ix)
                    else:
                        iz = NAN
                    z.append(iz)
                # this version does not support unordered x-values
                #dominio = x>=0
                #x_pos = x[dominio]
                #z_pos = f(x_pos)
                #z_neg = zeros(sum(~dominio))
                #z_neg[:] = NAN
                #z = append(z_neg, z_pos)
            else:
                print("Error en el tipo de variable ingresada")
                return
            return z
        return wrapper        
    return inner


def f1(x):
    z = exp(x) - 3*x**2
    return z

def df1(x):
    z = exp(x) - 6*x
    return z

@pos
def g1(x):
    z = log(3*x**2)
    return z

@pos
def f2(x):
    z = sqrt(x) - cos(x)
    return z
 
@pos
def df2(x):
    z = 1/(2*sqrt(x)) + sin(x)
    return z

def g2(x):
    z = cos(x)**2
    return z

def f3(x):
    z = exp(x) + 2**x + 2*cos(x) - 6
    return z

def df3(x):
    z = exp(x) + 2 - 2*sin(x)
    return z

def g3(x):
    z = log(- 2**x - 2*cos(x) + 6 )
    return z

@threshold(shift=1)
def f4(x):
    z = log(x-1) + cos(x-1)
    return z

@pos
def df4(x):
    z = 1/(x-1) - sin(x-1)
    return z

@pos
def g4(x):
    z = exp(- cos(x-1)) + 1
    return z

def inversa(x):
    return 1/x

