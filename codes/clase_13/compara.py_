# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x=np.linspace(1,3,100)
f=1/x
p=np.zeros(100)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

plt.plot(x,f,'b',label='función original')
for n in range(6):
    p=p+(-1)**n*(x-1)**n
    ax.plot(x,p,color=[n/5,1-n/5,0],label='$p_{%i}$'%n)
    #plt.plot([x[66],x[66]],[f[66],p[66]],'c')
    #plt.text(x[66],f[66],'error=%f'%(abs(p[66]-f[66])))
ax.legend()


# %%
x0=2; x1=5
x=np.array([0,7])
plt.figure()
plt.axes().set_aspect('equal')
plt.plot(x,(x-x1)/(x0-x1),'b',label='$L_0$')
plt.plot(x,(x-x0)/(x1-x0),'c',label='$L_1$')
plt.plot([0,7],[0,0],'k')
plt.plot([0,0],[-1,2],'k')
plt.plot([x0,x0,0],[0,1,1],'k:')
plt.plot([x1,x1,0],[0,1,1],'k:')
plt.xticks([x0,x1],['$x_0$','$x_1$'])
plt.yticks([0,1])
plt.legend()


# %%
def Lk(x,k):
    L=1
    for i in range(len(xdato)):
        if i!=k:
            L=L*(x-xdato[i])/(xdato[k]-xdato[i])
        return L

xdato=[0,1,1.5,2,3,4,5,6,6.5,7,8]
Lvec=np.vectorize(Lk)
z=np.linspace(-0.01,8.01,200)
plt.figure()
plt.plot(z,Lvec(z,5))
plt.plot([-0.1,8.1],[0,0],'k')
plt.xticks([0,1,2,3,4,5,6,7,8],['$x_{0}$','$x_{1}$','...','$x_{k-1}$','$x_{k}$','$x_{k+1}$','...','$x_{n-1}$','$x_{n}$'])
plt.plot([4,4,-0.1],[0,1,1],'k:')
plt.title('$L_{k}$');

