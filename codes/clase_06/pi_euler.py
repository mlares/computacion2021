import math
from matplotlib import pyplot as plt

s=0
es = []
s_old=0
for k in range(1, 100):
    e = 1/k**2    
    es.append(e)
    s = s + e
    s_old = s
p = math.sqrt(6*s)
print(p)

plt.plot(es)
plt.yscale('linear')
plt.show()
