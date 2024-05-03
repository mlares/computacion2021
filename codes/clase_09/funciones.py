# Aquí guardamos nuestra colección de funciones

from numpy import cos, sin

def func01(x):
    return cos(x) - x

def func01_prima(x):
    return -sin(x) - 1

def func01_g(x):
    return cos(x)
