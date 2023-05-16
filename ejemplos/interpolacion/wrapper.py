import ecuaciones1D
import funciones

f = funciones.func01
df = funciones.func01_prima
g = funciones.func01_g

r = ecuaciones1D.biseccion(f, 0, 1)
print(r)

r = ecuaciones1D.newton(f, df, 1)
print(r)

r = ecuaciones1D.secante(f, 0.5, 1)
print(r)

r = ecuaciones1D.puntofijo(g, 1)
print(r)


# Ahora juguemos un poco con los parámetros opcionales

tols = {'tolerancia_x': 1.e-4,
        'tolerancia_f': 1.e-4,
        'tolerancia_N': 20}
print('')

r = ecuaciones1D.biseccion(f, 0, 1, **tols)
print(r)

r = ecuaciones1D.newton(f, df, 1, **tols)
print(r)

r = ecuaciones1D.secante(f, 0.5, 1, **tols)
print(r)

r = ecuaciones1D.puntofijo(g, 1, **tols)
print(r)
        
# Ahora veamos los históricos y hagamos algunos plots

tols = {'tolerancia_x': 1.e-4,
        'tolerancia_f': 1.e-4,
        'tolerancia_N': 20,
        'historico': True}
print('')

rb = ecuaciones1D.biseccion(funciones.func01, 0, 1, **tols)
print(r)

rn = ecuaciones1D.newton(funciones.func01, funciones.func01_prima, 1, **tols)
print(r)

rs = ecuaciones1D.secante(funciones.func01, 0.5, 1, **tols)
print(r)

rp = ecuaciones1D.puntofijo(funciones.func01_g, 1, **tols)
print(r)


from matplotlib import pyplot as plt

plt.plot(rb.xlist, f(rb.xlist), marker='.', color='orange', linestyle='None')
plt.plot(rn.xlist, f(rn.xlist), marker='.', color='peru', linestyle='None')
plt.plot(rs.xlist, f(rs.xlist), marker='.', color='navy', linestyle='None')
plt.plot(rp.xlist, f(rp.xlist), marker='.', color='cadetblue', linestyle='None')
plt.show()



style = {'marker': 'o', 'markerfacecolor':'white', 'linestyle': 'None'}

plt.plot(rb.xlist, color='orange', label='bisección')
plt.plot(rn.xlist, color='peru', label='newton')
plt.plot(rs.xlist, color='navy', label='secante')
plt.plot(rp.xlist, color='cadetblue', label='puntofijo')
plt.legend()
plt.xlabel('Número de pasos')
plt.ylabel(r'Aproximación de $\bar{x}$')
plt.show()

            

# Ahora todo con una sola función

r = ecuaciones1D.aprox_raiz(f, df=df, g=g, 
                            metodo='biseccion',
                            intervalo=[0, 1], x0=1, xaux=0.5)

metodos = ['bisección', 'newton', 'secante', 'punto fijo']

for m in metodos:
    r = ecuaciones1D.aprox_raiz(f, df=df, g=g, metodo=m,
                                intervalo=[0, 1], x0=1, xaux=0.5)
    print(r.x)


rs = ecuaciones1D.aproxs_raiz(f, df=df, g=g, metodos=metodos,
                 intervalo=[0, 1], x0=1, xaux=0.5)

print(rs)

