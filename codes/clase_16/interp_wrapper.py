import interp_tools as it
import funciones as f

import numpy as np
from matplotlib import pyplot as plt
from functools import partial
from scipy import stats

it.comparar(f.inversa, -10, 10, 12, 300, 'plot1', -10.2, 10.2)

it.comparar(f.inversa, 1, 10, 12, 300, 'plot2', 0.9, 10.1)

N = partial(stats.norm.pdf, loc=0, scale=1)
it.comparar(N, -10, 10, 12, 300, 'plot3')

f = partial(np.polynomial.polynomial.polyval, c=[0, 0, 2])
it.comparar(f, -10, 10, 5, 300, 'plot4', -12, 12)

f = partial(np.polynomial.polynomial.polyval, c=[-1, -1, 0, 1, 0, 3])
it.comparar(f, -10, 10, 5, 300, 'plot5', -12, 12)

f = partial(np.polynomial.polynomial.polyval, c=[-1, -1, 0, 1, 0, 3])
it.comparar(f, -10, 10, 25, 300, 'plot6')



