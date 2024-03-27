# %%
import math
from matplotlib import pyplot as plt

from utils import (color_diff,
                   compute_pi_arctan,
                   compute_pi_gauss_legendre,
                   compute_pi_gauss_legendre_bits,
                   pi_1k)


# %% Calcular pi con 64 bits (estandar de python)
# Método: Serie de Taylor de arctan

for Niter in [100, 1000, 10000]:
    p = compute_pi_arctan(Niter)
    print(f'Serie de Taylor, 64 bits, {Niter} iteraciones')
    color_diff(f'{p:.100f}', pi_1k()[:100])

# %%
# Método: Gauss-Legendre
# https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm#:~:text=The%20Gauss%E2%80%93Legendre%20algorithm%20is,million%20correct%20digits%20of%20%CF%80.

for Niter in [5, 10, 15, 25]:
    pi = compute_pi_gauss_legendre(Niter)
    print(f'Gauss-Legendre, 64 bits, {Niter} iteraciones')
    color_diff(f'{pi:.100f}', pi_1k()[:100])

# %%

for Niter in [5, 10, 15, 25]:
    pi = compute_pi_gauss_legendre_bits(Niter, 16)
    print(f'Gauss-Legendre, 64 bits, {Niter} iteraciones')
    color_diff(f'{pi:.100f}', pi_1k()[:100])

# %%

Niter = 20
for prec in [4, 8, 16, 32, 64, 128]:
    pi = compute_pi_gauss_legendre_bits(Niter, prec)
    print(f'Gauss-Legendre, {prec} bits, {Niter} iteraciones')
    color_diff(f'{pi:.100f}', pi_1k()[:100])
