import ecuaciones1D as s
x1 = 20
x2 = 30
H = 8

def F(x, x1, x2, H):
    return x**3 * (x-4*H) - (x1**2-x2**2)**2
from functools import partial

f = partial(F, x1=x1, x2=x2, H=H)

s.biseccion(f, 0, 100)

r = s.biseccion(f, 30, 40)
x = r.x

def G(A, x, x1, x2):
    import math
    return A + math.sqrt(A**2-(x1**2-x2**2)) - x
g = partial(G, x=x, x1=x1, x2=x2)

R = s.biseccion(g, 10, 20)
A = R.x

import math
W = math.sqrt(x1**2 - A**2)
