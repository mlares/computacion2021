import numpy as np

xi = (-1,0,1,2)
yi = (-2,0,2,5)

D = np.zeros((len(yi),len(yi)))


for i in range(len(yi)):
    d0 = yi[0] #i=0
    

    d1 = (yi[1]-yi[0]) / (xi[1]-xi[0]) #i=1
    

    c1 = (yi[2]-yi[1]) / (xi[2]-xi[1])
    

    c11 = (yi[3]-yi[2]) / (xi[3]-xi[2])
    

    d2 = (c1-d1) / (xi[2]-xi[0]) #i=2


    c2 = (c11-c1) / (xi[3]-xi[1])
    

    d3 = (c2-d2) / (xi[3]-xi[0]) #i=3

print(d0,d1,d2,d3)

print()

d = (d0,d1,d2,d3)

for i in range(len(d)):
    D[i,i] = d[i]

print(D)

        
    