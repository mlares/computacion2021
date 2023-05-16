import numpy as np
from matplotlib import pyplot as plt

def V(t, R):
    from math import pi, sqrt
    D = 1 - t**2/(4*pi**2)
    Z = R**3/(12*pi) * t**2 * sqrt(D)
    return Z

def dV(t, R):
    from math import pi, sqrt
    c = R**3/(12*pi)
    D = 1 - t**2/(4*pi**2)
    T1 = 2*t*sqrt(D) 
    T2 = 2*t**3 / (4*pi**2) * D**(-0.5)
    Z = c * (T1 - T2)
    return Z


def V(t, R):
    from math import pi, sqrt
    D = 1 - t**2/(4*pi**2)
    c = R**3/(12*pi)
    Z = c * t**2 * sqrt(D)
    return Z
V = np.vectorize(V)

def dV(t, R):
    from math import pi, sqrt
    c = R**3/(12*pi)
    Discriminante = 1 - (t**2)/(4*pi**2)
    T1 = 2*t*sqrt(Discriminante) 
    T2 = t**3 / (2*pi**2) / sqrt(Discriminante)
    Z = c * (T1 - T2)

    Z2 = (8*pi**2*t - 3*t**3) / (2*pi*sqrt(4*pi**2 - t**2))

    return Z2
dV = np.vectorize(dV)


t = np.linspace(2, 6, 200)
R = 10

fig, ax = plt.subplots(2, 1)

ax[0].plot(t, V(t, R))
ax[1].plot(t, dV(t, R))
ax[1].axhline(0, color='silver', linewidth=2)

plt.show()
