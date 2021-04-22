

def csimpson(f, a, b, n):
    """Implementa la regla de Simpson compuesta.

    Arguments
    ---------
    f : function
        The function to be integrated.  It must be a python function
        that admits numpy arrays as arguments.
    a : float
        the left border of the interval
    b : float
        the right border of the interval
    n : integer
        the number of subintervals for the interval [a, b]

    Returns
    -------
    S : float
        An estimation of the integral of f in the interval [a, b]
        using the Simpson's rule
    """
    import numpy as np
    x, h = np.linspace(a, b, n, endpoint=True, retstep=True)
    S_par = 2 * f(x[2:n:2]).sum()
    S_imp = 4 * f(x[1:n:2]).sum()
    S = f(x[0]) + f(x[-1]) + S_par + S_imp
    S = S*h/3
    return S



def f(x):
    return x/4 * (10-x) + np.sin(np.pi*x)


I = csimpson(f, 0, 5, 10)


