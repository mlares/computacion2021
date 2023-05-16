import math as m
import matplotlib.pyplot as plt


def sFibo(N):
  F=[1,1]
  for n in range(N-1):
    F.append(F[n]+F[n+1])
  return F

F=sFibo(20)
n=len(F)-1; x=n*[0]
for i in range(n):
  x[i]=F[i+1]/F[i]
print(x)
print(x[-1])
print((1+m.sqrt(5))/2)

plt.figure()
plt.plot(x)
plt.title("x");   
plt.show()
