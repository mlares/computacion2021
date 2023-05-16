
def kepler(e, M, eps=1.e-6):
    # Calcular la anomalía media.

    from math import sin

    E_viejo = M
    D = e*sin(E_viejo)
    while D > eps:
        E_nuevo = E_viejo - e*sin(E_viejo)
        D = abs(E_viejo - E_nuevo)
        E_viejo = E_nuevo
    return E_viejo


from math import sin

e = 0.1
M = 2.5
E = kepler(e, M)
print(M, E - e*sin(E))

