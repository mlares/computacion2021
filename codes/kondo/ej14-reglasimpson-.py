#regla de simpson compuesta

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1/4)*x*(10-x)+ np.sin(np.pi*x)
a=0
b=5
N=5
h=(b-a)/N

def simpson(f,a,b,N, h):
    h = h / 2
    Xi=np.array([a+h*i for i in range(2*N+1)])
    Yi=f(Xi)
    suma1=sum(np.array([Yi[2*i] for i in range(1,N)]))
    suma2=sum(np.array([Yi[2*i+1] for i in range(N)]))
    simpson= (h/3)*(f(a)+2*suma1+4*suma2+f(b))
    print(simpson)
    
    return simpson

print("La aprox. de la integral por la regla de simpson compuesta es: ", simpson(f,a,b,N))

Xi= np.array([a+h*i for i in range(N)]) #para calcular la funcion
Yi= f(Xi)

xi=np.linspace(a,b,100) #Para graficar muchos puntos para f(x) y sea suave
yi=f(xi)

plt.title("Funcion y funcion escalon usada para integrar")
plt.xlabel("x")
plt.ylabel("y")
plt.step(Xi,Yi,'r') #funcion escalon
plt.plot(xi,yi,'b') #funcion f(x)

for j in range(len(Xi)):
    plt.plot(Xi[j], Yi[j],'go') #puntos (xi,yi)

plt.savefig("EjReglaDeSimpson.png")
plt.show()



N = 10
x = [1 * i for i in range(2*N+1)]
n1 = len(x)
n2 = len([x[2*i] for i in range(1,N)])
n3 = len([x[2*i+1] for i in range(N)])





