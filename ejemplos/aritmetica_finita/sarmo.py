import matplotlib.pyplot as plt
import math as m

def sarmo(N,p):    
  S=[1]; a=0
  n=1
  while n<=N:
    a=a+1/n
    S.append(a-p*m.log(n))
    n=n+1
  return S

Sp=sarmo(20,0.9)
print(Sp)
plt.figure()
plt.plot(Sp)
plt.title("S_n(p)"); 
plt.show()
