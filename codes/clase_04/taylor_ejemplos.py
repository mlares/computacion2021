import math as m

# fijemos un valor de n
n=17
# calculemos la suma1 y sus errores
s1=0;
for i in range(n+1):  #ojo, range(n)=[0,1,...,n-1] son n contando desde cero
  s1 = s1 + 1/m.factorial(i)
print('\nsuma_1 = ',s1)
print('error absoluto=',abs(s1-m.e))
print('error relativo=',abs(s1-m.e)/m.e)

# calculemos la suma2 y sus errores
s2=0;
for j in range(n+1):
  s2 = s2 + 1/m.factorial(n-j)
print('\nsuma_2 = ',s2)
print('error absoluto=',abs(s2-m.e))
print('error relativo=',abs(s2-m.e)/m.e)
print('')

# calculemos la suma2 y sus errores (de otra forma)
s2=0;
for j in range(n, -1, -1):
  s2 = s2 + 1/m.factorial(j)
print('\nsuma_2 = ',s2)
print('error absoluto=',abs(s2-m.e))
print('error relativo=',abs(s2-m.e)/m.e)
print('')
