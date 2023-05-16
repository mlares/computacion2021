import numpy as np
from matplotlib import pyplot as plt
import interp_tools as it

from numpy.polynomial import polynomial as P
from functools import partial

f = lambda x: 1/x

xd = np.array([2, 2.75, 4])
yd = f(xd)


xi = np.linspace(2, 4, 200)
ym = f(xi)

yl = it.interp_lagrange(xi, xd, yd)

fig = plt.figure(figsize=(6, 10))

ax = fig.add_subplot(321)
ax.plot(xi, yl, linewidth=1.4, linestyle='-', color='orchid', 
        label='lagrange')
ax.plot(xd, yd, marker='o', linestyle='None', color='navy', markersize=5)
ax.grid()
ax.legend()

ax = fig.add_subplot(322)

yxi = 1/xi**4
ax.plot(xi, yxi)
ax.plot(xi[0], yxi[0], 'o')
print(yxi[0])


ax = fig.add_subplot(323)

# el polinomio g
coefs = P.polyfromroots([2, 2.75, 4])
g = partial(P.polyval, c=coefs)

ax.plot(xi, np.absolute(g(xi)), label='función g(x)')
ax.grid()
ax.legend()

ax = fig.add_subplot(324)

# puntos críticos

coefs_prima = P.polyder(coefs)

gprima = partial(P.polyval, c=coefs_prima)

rs = P.polyroots(coefs_prima)

ax.plot(xi, gprima(xi), label=r'función g$_x$(x)')
ax.plot(rs[0], gprima(rs[0]), 'o')
ax.plot(rs[1], gprima(rs[1]), 'o')
ax.grid()
ax.legend()

print(rs[0])
print(rs[1])
print(g(rs[0]))
print(g(rs[1]))
print(9/16)

Em = yxi[0]*g(rs[1])


ax = fig.add_subplot(325)
ax.plot(xi, yl-ym, linewidth=1.4, color='orchid')

ax.plot(xd, [0]*len(xd), marker='o', linestyle='None', color='navy',
        markersize=3)
ax.axhline(Em, color='coral')
ax.axhline(-Em, color='coral')
delta = 2*Em*0.1
ax.set_ylim(-Em-delta, Em+delta)
ax.grid()

plt.tight_layout()
fig.savefig('plot_error.png')


