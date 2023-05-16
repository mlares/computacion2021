# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
def Lk(xdatos, x, k):
    L=1
    for i in range(len(xdatos)):
        if i!=k:
            L = L*(x-xdatos[i])/(xdatos[k]-xdatos[i])
    return L


# %%
xdatos = np.array([1, 1.5, 2, 3, 4, 5, 6, 6.5, 7,8])
ydatos = 1/xdatos

# %%
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.plot(xdatos, ydatos, 'o', markersize=9)


# %%
def P_lagrange(x, xdatos, ydatos):
    y = 0
    for k in range(len(ydatos)):
        y = y + ydatos[k]*Lk(xdatos, x, k)
    return y


# %%
x = 2.5
y = P_lagrange(x, xdatos, ydatos)


# %%
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.plot(xdatos, ydatos, 'o', markersize=9)
ax.plot(x, y, 'o', markersize=9)


# %%
x = np.linspace(1, 8, 100)
Lk(x, xdatos, 2)
# %%
y = P_lagrange(x, xdatos, ydatos)
# %%
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.plot(x, y, '-', markersize=9, color='cadetblue')
ax.plot(xdatos, ydatos, 'o', markersize=9, color='navy')
# %%

