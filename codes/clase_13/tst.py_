# %%
import numpy as np
from matplotlib import pyplot as plt

# %%
def NDD(x, y):
    """Devuelve las diferencias divididas de Newton.

    Args:
    x : lista o array
        Los valores de x
    y : lista o array
        Los valores de y
    Returns:
    NDD : array
        Array con las diferencias divididas
    """
    NDD = []
    N = len(x)
    M = np.zeros([N,N])
    M[:,0] = y
    
    for columna in range(1,N):
        for fila in range(N-columna):
    
            m = f"M[{fila}, {columna}]"
    
            ll = [m, f"= (M[{fila+1},{columna-1}]", '-', 
                     f"M[{fila}, {columna-1}])", '/',
                     f"(x[{fila+columna}] - x[{fila}])", '\n']
            print(''.join(ll))
    
            num = M[fila+1, columna-1] - M[fila, columna-1] 
            den = x[fila+columna] - x[fila]
            M[fila,columna] = num/den
                                                                 
    print('Matriz:')
    print(M)
    NDD = M[0,:]
    return NDD
# %%
def NDD_eval(x_sample, a, x):
    """Evaluar el polinomio interpolante.

    Args:
    a : array
        Diferencias divididas
    x_sample : list or array
        Valores donde quiero evaluar al polinomio
    x : list or array
        Valores X interpolados
    Returns:
    y : list or array
        Valores del polinomio en x
    """
    N = len(dd)
    print(f"P = a[{N-1}]")
    for i in range(N-2, -1, -1):
        print(f"P = a[{i}] + p*(x-x[{i}])")
                                             
    N = len(a)
    y = []
    for xx in x_sample:
        p = a[N-1]
        for i in range(N-2, -1, -1):
            p = a[i] + p*(xx-x[i])
        y.append(p)

    return y
# %%
x = [-1, 0, 1, 2]
y = [-10, -5, 1, 2]
              
dd = NDD(x, y)

xi = np.linspace(-1, 2, 100)
yi = NDD_eval(xi, dd, x)

fig = plt.figure(figsize=(12,8))
ax = 

plt.plot(x, y, 'ob')
plt.plot(xi, yi, 'r-')
plt.show()
# %%
