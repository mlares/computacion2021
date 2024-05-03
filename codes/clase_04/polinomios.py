import numpy as np
from matplotlib import pyplot as plt
import time
from random import random


def evalpol(c,x):
  """ Función para evaluar un polinomio.
  Para un polinomio p(x)= c_n x**n+c_{n-1} x**{n-1}+ ...+c_0
  c=[c_0, c_1, ..., c_n], vector de dimensión n+1 """
  p = 0
  n = len(c)
  for i in range(n):
    p = p + c[i] * x**i
  return p

def horner(c,x):
  # Función que implementa el método de Horner
  n = len(c) - 1
  p = c[n]
  for i in reversed(range(n)):
    p = p * x + c[i]
  return p      



coef = [1.5,3.2,-6.1,1]

x = np.linspace(-5, 5, 100)
y1 = evalpol(coef, x)
y2 = evalpol(coef, x)

x0 = 4.71e-2

print('Evaluar en un punto cualquiera y comparar los resultdos:')
print(f'P({x0}) = {evalpol(coef, x0)}')
print(f'P({x0}) = {horner(coef, x0)}')


x = np.array([random()*100 - 50 for _ in range(1000000)])

start = time.time()
r=evalpol(coef, x)
end = time.time()
print('Tiempo para la fórmula básica: ', end - start, 's')
time_bruteforce = end - start

start = time.time()
r=horner(coef, x)
end = time.time()
time_horner = end - start
print('Tiempo para la fórmula de horner: ', end - start, 's')

print(f'El método de Horner es {time_bruteforce/time_horner: .2f} veces más rápido')


# Nota en jupyter se puede usar %time

