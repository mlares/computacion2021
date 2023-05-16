import numpy as np
from fractions import Fraction as frac


class bcolors:
    # ANSI escape sequences
    # Ver también el paquete colorama
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TST = '\033[31;1m'
    X = '\033[4;95;1m'

def niceprint(matrix, ij=[None, None]):
    sp = ' '*50
    print(f'{bcolors.X}{sp}{bcolors.ENDC}\n')
    ki=0
    for irow, row in enumerate(matrix):
        pp = []
        for icol, rr in enumerate(row):
            if abs(rr)>1.e-8:
                r = frac(rr)
                if r.numerator > 1.e3 or r.denominator > 1.e3:
                    r = f'{rr:7.3f}'
                else:
                    r = str(frac(rr))
                if (ij[0]==irow) and (ij[1]==icol):
                    r = f'{bcolors.OKGREEN}{r}{bcolors.ENDC}'
            else:
                r = '0'
            pp.append(r)
        p = pp[:-1]
        p.append(f'{bcolors.WARNING}:{bcolors.ENDC}')
        p.append(f'{bcolors.TST}{pp[-1]}{bcolors.ENDC}')
        msg = "\t".join(p)           
        print(msg)
        print("\u001b[0m")  # reset
    return 0

def operador(i, j, mu=None, f=None, n=3):
    """
    Construye un operador matricial para la operacion:
    F[f] ← F[i] + mu*F[j]
    """
    M = np.eye(n)
    if mu is None:
        # permutar filas
        aux = M[i,:].copy()
        M[i,:] = M[j,:]
        M[j,:] = aux
    else:
        nuevafila = M[i,:] + mu*M[j,:]
        M[f,:] = nuevafila
    return M 

def show_eqs(A, B):
    for a, b in zip(A, B):
        s = ''
        for i, aa in enumerate(a):

            if abs(aa)>1.e-12:
                aij = f'{aa}*x{i+1} + ' 
            else:
                aij = ' '*6
            s = s + aij
        s = s[:-2] + f' = {b}'
        print(s) 
