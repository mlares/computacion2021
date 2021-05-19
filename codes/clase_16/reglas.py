{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fatty-container",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cuad_pmedio(a, b, f):\n",
    "    \"\"\"Implementación de la regla del punto medio\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    f: La función a integrar\n",
    "    a: Límite inferior del intervalo\n",
    "    b: Límite superior del intervalo\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla del punto medio\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    \"\"\"\n",
    "    if a > b:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "        return None\n",
    "    try:\n",
    "        x0 = (a+b)/2\n",
    "        h = f(x0)\n",
    "        aprox = h*(b-a)\n",
    "    except:\n",
    "        print('Error: no fue posible calcular la función')\n",
    "    return aprox\n",
    "\n",
    "def cuad_trapecio(a, b, f):\n",
    "    \"\"\"Implementación de la regla del trapecio\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    f: La función a integrar\n",
    "    a: Límite inferior del intervalo\n",
    "    b: Límite superior del intervalo\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla del trapecio\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    \"\"\"\n",
    "    if a > b:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "        return None\n",
    "    try:\n",
    "        h = f(a) + f(b)\n",
    "        aprox = (b-a)/2*h\n",
    "    except:\n",
    "        print('Error: no fue posible calcular la función')\n",
    "    return aprox\n",
    "\n",
    "def cuad_simpson(a, b, f):\n",
    "    \"\"\"Implementación de la regla de Simpson\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    f: La función a integrar\n",
    "    a: Límite inferior del intervalo\n",
    "    b: Límite superior del intervalo\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla de Simpson\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    \"\"\"\n",
    "    if a > b:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "        return None\n",
    "    try:\n",
    "        x0 = (a+b)/2\n",
    "        h = f(a) + f(b) + 4*f(x0)\n",
    "        aprox = (b-a)/6*h\n",
    "    except:\n",
    "        print('Error: no fue posible calcular la función')\n",
    "    return aprox\n",
    "\n",
    "def f(x):\n",
    "    return x**2\n",
    "\n",
    "I = cuad_pmedio(1, 2, f)\n",
    "print(f'La regla del punto medio da como resultado: {I}')\n",
    "\n",
    "I = cuad_trapecio(1, 2, f)\n",
    "print(f'La regla del trapecio da como resultado: {I}')\n",
    "\n",
    "I = cuad_simpson(1, 2, f)\n",
    "print(f'La regla de simpson da como resultado: {I}')\n",
    "\n",
    "\n",
    "\n",
    "def cuad_pmedio(a, b, y0):\n",
    "    \"\"\"Implementación de la regla del punto medio\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    f: La función a integrar\n",
    "    a: Límite inferior del intervalo\n",
    "    b: Límite superior del intervalo\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla del punto medio\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    \"\"\"\n",
    "    try:\n",
    "        x0 = (a+b)/2\n",
    "        aprox = x0*y0\n",
    "    except:\n",
    "        print('Error: no fue posible calcular la función')\n",
    "    return aprox\n",
    "\n",
    "cuad_pmedio(0, 1, 0.5)\n",
    "\n",
    "def cuad_pmedio(a, b, f=None, y0=None):\n",
    "    \"\"\"Implementación de la regla del punto medio\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    a: float\n",
    "       Límite inferior del intervalo\n",
    "    b: float\n",
    "       Límite superior del intervalo\n",
    "    f: function (1 parameter)\n",
    "       La función a integrar\n",
    "    y0: float\n",
    "       El valor de y en el punto medio.\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla del punto medio\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    \"\"\"\n",
    "    if a > b:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "\n",
    "    x0 = (a+b)/2\n",
    "    if (f is None) and (y0 is not None):\n",
    "            aprox = x0*y0\n",
    "    elif (f is not None) and (y0 is None):            \n",
    "        try:\n",
    "            h = f(x0)\n",
    "        except:\n",
    "            print(('Error: no fue posible calcular la función'\n",
    "                   ' Si desea ingresar un dato use y0='))\n",
    "        aprox = h*(b-a)\n",
    "\n",
    "    else:\n",
    "        raise ValueError(\"Debe ingresar la función o los datos!\")            \n",
    "            \n",
    "    return aprox\n",
    "\n",
    "cuad_pmedio(0, 1, y0=0.5)\n",
    "\n",
    "def cuad_trapecio(x0, x1, f=None, y0=None, y1=None):\n",
    "    \"\"\"Implementación de la regla del trapecio\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    x0: float\n",
    "       Límite inferior del intervalo\n",
    "    x1: float\n",
    "       Límite superior del intervalo\n",
    "    f: function (1 parameter)\n",
    "       La función a integrar\n",
    "    y0: float\n",
    "       El valor de y en el punto medio.\n",
    "    y1: float\n",
    "       El valor de y en el punto medio.\n",
    "\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla del punto medio\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    Uso:  \n",
    "        cuad_trapecio(x0, x1, f=f)\n",
    "        cuad_trapecio(x0, x1, y0=f(x0), y1=f(x1))\n",
    "    \"\"\"\n",
    "    if x0 > x1:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "\n",
    "    if (f is None) and (y0 is not None) and (y1 is not None):\n",
    "            aprox = (x1-x0)*(y0+y1)/2\n",
    "    elif (f is not None) and (y0 is None):            \n",
    "        try:\n",
    "            y0 = f(x0)\n",
    "            y1 = f(x1)\n",
    "        except:\n",
    "            print(('Error: no fue posible calcular la función'\n",
    "                   ' Si desea ingresar un dato use y0='))\n",
    "        aprox = (x1-x0)*(y0+y1)/2\n",
    "\n",
    "    else:\n",
    "        raise ValueError(\"Debe ingresar la función o los datos!\")            \n",
    "            \n",
    "    return aprox\n",
    "\n",
    "cuad_trapecio(0, 1, f)\n",
    "\n",
    "cuad_trapecio(0, 1, y0=f(0), y1=f(1))\n",
    "\n",
    "def contar_argumentos(func):\n",
    "    def inner(*args, **kwargs):\n",
    "        nargs_in = len(args) + len(kwargs)\n",
    "        return func(*args, **kwargs, nargs_in=nargs_in)\n",
    "    return inner\n",
    "\n",
    "\n",
    "\n",
    "@contar_argumentos\n",
    "def cuad_trapecio(x0, x1, f=None, y0=None, y1=None, nargs_in=None):\n",
    "    \"\"\"Implementación de la regla del trapecio\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    x0: float\n",
    "       Límite inferior del intervalo\n",
    "    x1: float\n",
    "       Límite superior del intervalo\n",
    "    f: function (1 parameter)\n",
    "       La función a integrar\n",
    "    y0: float\n",
    "       El valor de y en el punto medio.\n",
    "    y1: float\n",
    "       El valor de y en el punto medio.\n",
    "\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla del punto medio\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    Uso:  \n",
    "        cuad_trapecio(x0, x1, f=f)\n",
    "        cuad_trapecio(x0, x1, y0=f(x0), y1=f(x1))\n",
    "    \"\"\"\n",
    "    if nargs_in==4:\n",
    "        y1=y0        \n",
    "        y0=f\n",
    "        f = None\n",
    "    elif nargs_in==3:\n",
    "        if type(f) is float:        \n",
    "            raise ValueError(\"Verificar los argumentos\")\n",
    "    else:\n",
    "        raise ValueError(\"Verificar el número de argumentos\")\n",
    "            \n",
    "    if x0 > x1:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "\n",
    "    if (f is None) and (y0 is not None) and (y1 is not None):\n",
    "            aprox = (x1-x0)*(y0+y1)/2\n",
    "    elif (f is not None) and (y0 is None):            \n",
    "        try:\n",
    "            y0 = f(x0)\n",
    "            y1 = f(x1)\n",
    "        except:\n",
    "            print(('Error: no fue posible calcular la función'\n",
    "                   ' Si desea ingresar un dato use y0='))\n",
    "        aprox = (x1-x0)*(y0+y1)/2\n",
    "\n",
    "    else:\n",
    "        raise ValueError(\"Debe ingresar la función o los datos!\")            \n",
    "            \n",
    "    return aprox\n",
    "\n",
    "cuad_trapecio(0, 1, f)\n",
    "\n",
    "cuad_trapecio(0, 1, f(0), f(1))\n",
    "\n",
    "@contar_argumentos\n",
    "def cuad_simpson(x0, x2, f=None, y0=None, y1=None, y2=None, nargs_in=None):\n",
    "    \"\"\"Implementación de la regla de simpson\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    x0: float\n",
    "       Límite inferior del intervalo\n",
    "    x2: float\n",
    "       Límite superior del intervalo\n",
    "    f: function (1 parameter)\n",
    "       La función a integrar\n",
    "    y0: float\n",
    "       El valor de y en el punto medio.\n",
    "    y2: float\n",
    "       El valor de y en el punto medio.\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla de Simpson\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    Uso:  \n",
    "        cuad_simpson(x0, x2, f=f)\n",
    "        cuad_simpson(x0, x2, y0=f(x0), y2=f(x2))\n",
    "        cuad_simpson(x0, x2, f)\n",
    "        cuad_simpson(x0, x2, y0, y2)\n",
    "    \"\"\"\n",
    "    \n",
    "    if nargs_in==5:\n",
    "        y2=y1\n",
    "        y1=y0\n",
    "        y0=f\n",
    "        f = None\n",
    "    elif nargs_in==3:\n",
    "        if type(f) is float:        \n",
    "            raise ValueError(\"Verificar los argumentos\")\n",
    "    else:\n",
    "        raise ValueError(\"Verificar el número de argumentos\")\n",
    "            \n",
    "    if x0 > x2:\n",
    "        raise ValueError(\"Oops!  Debe ser a<b\")\n",
    "        \n",
    "    x1 = (x0+x2)/2\n",
    "\n",
    "    if (f is None) and (y0 is not None) and (y1 is not None):\n",
    "            aprox = (x2-x0)/6 * (y0 + 4*y1 + y2)\n",
    "    elif (f is not None) and (y0 is None):            \n",
    "        try:\n",
    "            y0 = f(x0)\n",
    "            y1 = f(x1)\n",
    "            y2 = f(x2)\n",
    "        except:\n",
    "            print(('Error: no fue posible calcular la función'\n",
    "                   ' Si desea ingresar un dato use y0='))\n",
    "        aprox = (x2-x0)/6 * (y0 + 4*y1 + y2)\n",
    "\n",
    "    else:\n",
    "        raise ValueError(\"Debe ingresar la función o los datos!\")            \n",
    "            \n",
    "    return aprox\n",
    "\n",
    "cuad_simpson(0, 1, f)\n",
    "\n",
    "cuad_simpson(0, 1, f(0), f(0.5), f(1))\n",
    "\n",
    "\n",
    "\n",
    "import numpy as np\n",
    "x = np.linspace(0, 10, 11)\n",
    "\n",
    "x\n",
    "\n",
    "np.diff(x)\n",
    "\n",
    "def cuad_simpson_compuesta(x, f=None, y=None):\n",
    "    \"\"\"Implementación de la regla de simpson\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    x: list or array\n",
    "       Lista de valores de x\n",
    "    f: function (1 parameter)\n",
    "       La función a integrar\n",
    "    y: list or array\n",
    "       La lista de valores de y\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla de Simpson\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    Uso:  \n",
    "        cuad_simpson(x, y=y)\n",
    "        cuad_simpson(x, f=f)\n",
    "    \"\"\"\n",
    "    import numpy as np\n",
    "\n",
    "    # Primero verificar si la particion es regular    \n",
    "    x = np.array(x)\n",
    "    x.sort()    \n",
    "    H = (max(x) - min(x))/len(x-1)\n",
    "    equiesp = np.std(np.diff(x)) < H*1.e-6\n",
    "    \n",
    "    # Calcular los valores de y (si se pasó una función)\n",
    "    if (y is None) and (f is not None):\n",
    "        y = f(x)\n",
    "        \n",
    "    n = len(x)\n",
    "    \n",
    "    if equiesp:        \n",
    "        impares = y[1:-1:2].sum()\n",
    "        pares = y[2:-1:2].sum()        \n",
    "        H = y[0] + 2*pares + 4*impares + y[-1] \n",
    "        H = H / (3*n)\n",
    "        aprox = (x[-1]-x[0])*H\n",
    "    else:\n",
    "        aprox = 0\n",
    "        for i in range(0, len(x)-2, 2):\n",
    "            aprox += cuad_simpson(x[i], x[i+2], y[i], y[i+1], y[i+2])\n",
    "            \n",
    "    return aprox\n",
    "\n",
    "def f(x):\n",
    "    return x**2\n",
    "\n",
    "x = np.linspace(0, 1, 999)\n",
    "xr = np.random.uniform(0, 1, 1000)\n",
    "y = f(x)\n",
    "yr = f(xr)\n",
    "\n",
    "cuad_simpson_compuesta(x, y=y)\n",
    "\n",
    "cuad_simpson_compuesta(xr, y=yr)\n",
    "\n",
    "cuad_simpson_compuesta(x, f=f)\n",
    "\n",
    "from scipy import integrate\n",
    "\n",
    "integrate.quad(f, 0, 1)\n",
    "\n",
    "##### Otra opción sería dar el intervalo y la función, e ir achicando la norma de la partición hasta que el error sea menor que algún valor dado.\n",
    "\n",
    "def cuad_simpson_compuesta_II(f, I, eps):\n",
    "    \"\"\"Implementación de la regla de Simpson\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    I: list\n",
    "       Intervalo de integración, ingresado como lista de dos elementos\n",
    "    f: function (1 parameter)\n",
    "       La función a integrar\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    aprox: Aproximación de la integral por la regla de Simpson\n",
    "    \n",
    "    Notes\n",
    "    -----\n",
    "    Este código es parte del curso \"Computación\", Famaf\n",
    "    Uso:  \n",
    "        cuad_simpson_compuesta_II(f, I)\n",
    "        cuad_simpson_compuesta_II(f, I)\n",
    "    \"\"\"\n",
    "    import numpy as np\n",
    "\n",
    "    delta = 2*eps\n",
    "    n = 2\n",
    "    aprox_old = (I[1]-I[0])*f((I[1]+I[0])/2)\n",
    "\n",
    "    while delta > eps:\n",
    "        x = np.linspace(I[0], I[1], n)\n",
    "        aprox = cuad_simpson_compuesta(x, f=f)\n",
    "        delta = abs(aprox - aprox_old)\n",
    "        aprox_old = aprox\n",
    "        n += 10\n",
    "        if n>5000:\n",
    "            break\n",
    "\n",
    "    return aprox\n",
    "\n",
    "I = cuad_simpson_compuesta_II(f, [0, 1], 1.e-6)\n",
    "\n",
    "I"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}