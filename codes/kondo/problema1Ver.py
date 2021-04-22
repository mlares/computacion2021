# PROBLEMA 1

import numpy as np


A = np.array([[4,2,5],[2,5,8],[5,4,3]])

b = np.array([60.7,92.9,56.3])

N = len(b)


for i in range(0,N-1,1):
    for k in range(i,N):
        if A[k,i] != 0 and k != i:
            aux = np.copy(A[i,:])
            A[i,:] = np.copy(A[k,:])
            A[k,:] = np.copy(aux)
            
A1 = np.copy(A)

#print('Pivoteo parcial por filas')   
print(A1)
print()

for i in range(0,N-1,1):
    for j in range(i+1,N):
         mji = A[j,i] / A[i,i]
         A[j,:] = A[j,:] - mji * A[i,:]

print("Matriz Triangular Superior")
print(A)

print(A,b)

def trsup(A,b):
    N = len(b)

    Ab = np.concatenate((A,b),axis=1)
 
    for i in range(0,N-1,1):
        for k in range(i,N):
            if Ab[k,i] != 0 and k != i:
                aux = np.copy(Ab[i,:])
                Ab[i,:] = np.copy(Ab[k,:])
                Ab[k,:] = np.copy(aux)  
    
    x = np.zeros(N)   
    for i in range(N-1,-1,-1):
        xsum = 0 
        for j in range(i+1,N,1):
            xsum += Ab[i,j] * x[j]
        x[i] = (b[i] - xsum) / Ab[i,i]
    return x

x = trsup(A,b)

print('x = ',x)


x = np.zeros(N)


for i in range(N-1,-1,-1):
    xsum = 0
    for j in range(i+1,N,1):
        xsum += Ab[i,j] * x[j]
    x[i] = (Ab[i,N] - xsum) / Ab[i,i]



