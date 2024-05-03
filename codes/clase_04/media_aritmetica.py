import matplotlib.pyplot as plt
import math as m


def agm(x,y):
  error=1e-16
  a=[x]; b=[y]
  k=0
  criterio=True
  while criterio:
    a.append((a[k]+b[k])/2)
    b.append(m.sqrt(a[k]*b[k]))
    k=k+1
    criterio=(a[k]-b[k]>error)
  return [a,b]


x = m.sqrt(2)
y = 1.

salida=agm(x, y)
print(salida)

nit=len(salida[0])
E=nit*[0]
for n in range(nit):
  E[n]=salida[0][n]-salida[1][n]
print(E)

Elin=(nit-1)*[0]
Ecuad=(nit-1)*[0]
for n in range(nit-1):
  Elin[n]=E[n+1]/E[n]
  Ecuad[n]=E[n+1]/E[n]**2
print(Elin)
print(Ecuad)


plt.figure()
plt.subplot(1, 2, 1) # (filas, columnas, nro de panel)
plt.plot(salida[0], marker='o', color='teal')
plt.plot(salida[1], marker='o', color='chocolate')
plt.title("sucesiones")

plt.subplot(1, 2, 2)
plt.plot(E, marker='o', color='slategrey');
plt.title("error")




plt.figure()
plt.subplot(1, 2, 1)
plt.plot(Elin, marker='o', color='slategrey')
plt.title("error lineal")
plt.subplot(1, 2, 2)
plt.plot(Ecuad, marker='o', color='slategrey')
plt.title("cuadrático")

plt.show()
