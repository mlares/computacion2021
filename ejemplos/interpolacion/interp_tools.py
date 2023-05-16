def Lk(xdatos, x, k):
    L=1
    for i in range(len(xdatos)):
        if i!=k:
            L = L*(x-xdatos[i])/(xdatos[k]-xdatos[i])
    return L

def interp_lagrange(x, xd, yd):
    y = 0
    for k in range(len(yd)):
        y = y + yd[k]*Lk(xd, x, k)
    return y

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
    from numpy import zeros
    NDD = []
    N = len(x)
    M = zeros([N,N])
    M[:,0] = y
    
    for columna in range(1,N):
        for fila in range(N-columna):
    
            m = f"M[{fila}, {columna}]"
    
            ll = [m, f"= (M[{fila+1},{columna-1}]", '-', 
                     f"M[{fila}, {columna-1}])", '/',
                     f"(x[{fila+columna}] - x[{fila}])", '\n']
            #print(''.join(ll))
    
            num = M[fila+1, columna-1] - M[fila, columna-1] 
            den = x[fila+columna] - x[fila]
            M[fila,columna] = num/den
                                                                 
    NDD = M[0,:]
    return NDD

def NDD_eval(xi, dd, xd):
    """Evaluar el polinomio interpolante.

    Args:
    dd : array
        Diferencias divididas
    xi : list or array
        Valores donde quiero evaluar al polinomio
    xd : list or array
        Valores X interpolados
    Returns:
    y : list or array
        Valores del polinomio en x
    """
    #N = len(dd)
    #print(f"P = a[{N-1}]")
    #for i in range(N-2, -1, -1):
        #print(f"P = a[{i}] + p*(x-x[{i}])")
                                             
    N = len(dd)
    y = []
    for xx in xi:
        p = dd[N-1]
        for i in range(N-2, -1, -1):
            p = dd[i] + p*(xx-xd[i])
        y.append(p)

    return y

def interp_newton(x, xd, yd):
    dd = NDD(xd, yd)
    y = NDD_eval(x, dd, xd)
    return y

def comparar(f, xmin, xmax, ndata, ninterp, 
             fname='plot', ximin=None, ximax=None):

    from numpy import linspace
    from matplotlib import pyplot as plt

    xd = linspace(xmin, xmax, ndata)
    yd = f(xd)
    if ximin is None:
        ximin=xmin
    if ximax is None:
        ximax=xmax
        
    xi = linspace(ximin, ximax, ninterp)
    ym = f(xi)
    yl = interp_lagrange(xi, xd, yd)
    yn = interp_newton(xi, xd, yd)

    fig = plt.figure(figsize=(6, 10))

    ax = fig.add_subplot(311)
    ax.plot(xi, ym, linewidth=4, color='silver', label='modelo')
    ax.plot(xi, yl, linewidth=1.4, linestyle='-', color='orchid', 
            label='lagrange')
    line, = ax.plot(xi, yn, linewidth=1.4, linestyle='--', color='dodgerblue', 
            label='newton')
    line.set_dashes([10, 10, 10, 10])
    ax.plot(xd, yd, marker='o', linestyle='None', color='navy', markersize=5)
    ax.grid()
    ax.legend()

    ax = fig.add_subplot(312)
    ax.plot(xi, yl-ym, linewidth=1.4, color='dodgerblue', label='newton')
    line, = ax.plot(xi, yn-ym, linewidth=1.4, color='orchid', label='lagrange')
    line.set_dashes([10, 10, 10, 10])

    ax.plot(xd, [0]*len(xd), marker='o', linestyle='None', color='navy',
            markersize=3)
    ax.grid()
    ax.legend()

    ax = fig.add_subplot(313)
    ax.plot(xi, yn-yl, linewidth=1.0, color='black', label='difference')
    ax.grid()
    ax.legend()

    plt.tight_layout()
    filename = '.'.join([fname, 'png'])
    fig.savefig(fname)

    return None



