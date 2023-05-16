import numpy as np
from matplotlib import pyplot as plt

# modelo
def f(x):
    from math import exp
    y = 10000*exp(x) + 5000/x*(exp(x)-1)
    y = y - 40000
    return y

# graficar

x = np.linspace(0.01, 2, 100)
y = [f(_) for _ in x]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y)
ax.set_xlabel('x')



from scipy.optimize import brentq
root = brentq(f, 0.01, 2)
print(root)

ymin, ymax = ax.get_ylim()
ax.plot([root, root], [0, ymin], linewidth=0.4)

plt.show()

