import numpy as np

#Matriz Triangular Superior

A = np.array([[4,2,5],[2,5,8],[5,4,3]])
b = np.array([[60.7],[92.9],[56.3]])

def f(A, b):

    Ab = np.concatenate((A,b),axis=1)
    N = len(b)

    for i in range(0,N-1,1):
        for k in range(i,N):
            if Ab[k,i] != 0 and k != i:
                aux = np.copy(Ab[i,:])
                Ab[i,:] = np.copy(Ab[k,:])
                Ab[k,:] = np.copy(aux)

    print(Ab)
                
    for i in range(0,N-1,1):
        for j in range(i+1,N):
             mji = Ab[j,i] / Ab[i,i]
             Ab[j,:] = Ab[j,:] - mji * Ab[i,:]
             
    print(Ab)
                
    x = np.zeros(N)
    for i in range(N-1,-1,-1):
        xsum = 0
        for j in range(i+1,N,1):
            xsum += Ab[i,j] * x[j]
        x[i] = (Ab[i,N] - xsum) / Ab[i,i]
        
    x = np.transpose([x])
    return x


print(f(A, b))

xsol = np.linalg.solve(A,b)
print(xsol)
