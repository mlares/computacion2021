import matplotlib.pyplot as plt
import math as m

N=120
x=[5]; y=[5]
for n in range(1,N):
  x.append((n+1)/n**2)
  y.append((n+3)/n**3)
#print(x)
#print(y)
plt.figure()
plt.plot(x)
plt.plot(y)
#plt.xscale('log')
#plt.yscale('log')
plt.title("{xn}, {yn}");
plt.show()
