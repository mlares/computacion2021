from functools import partial
import ecuaciones1D as s
from matplotlib import pyplot as plt
from matplotlib import patches
from numpy import linspace

def y(x, r):
    from numpy import sqrt
    return r - sqrt(r**2 - (x-r)**2)

a=0.75
b=0.5

def G(r, a, b):
    from math import sqrt
    z = sqrt(r**2 - (r-a)**2) + b
    return z

g = partial(G, a=a, b=b)
s.puntofijo(g, 0.5)
R = s.puntofijo(g, 0.5)

x = linspace(0, R.x, 500)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.plot(x, y(x, R.x))
ax.plot([a], [b], '*')
ax.set_aspect('equal', 'box')

rect = patches.Rectangle((0,0),a,b, edgecolor='r', facecolor="none")
ax.add_patch(rect)

plt.show()
