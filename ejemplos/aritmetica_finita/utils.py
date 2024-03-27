import math
import decimal
import colorama

"""
Funciones utiles para comparar la precision en el calculo de pi
con modulo *decimal*
Referencia:
https://www.pythonforbeginners.com/basics/decimal-module-in-python
"""

def color_diff(string1, string2):
    from colorama import Fore, Back, Style
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            print(f'{Fore.RED}{char1}', end="")
        else:
            print(f'{Fore.GREEN}{char1}', end="")
    print()
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            print(f'{Fore.RED}{char2}', end="")
        else:
            print(f'{Fore.GREEN}{char2}', end="")
    print('\n')
    print(Style.RESET_ALL)



def compute_pi_arctan(Niter):
    s=0
    es = []
    s_old=0
    for k in range(1, Niter):
        e = 1/k**2
        es.append(e)
        s = s + e
        s_old = s
    p = math.sqrt(6*s)
    return p

def compute_pi_gauss_legendre(Niter):
    a = 1
    b = 1/math.sqrt(2)
    t = 1/4
    p = 1
    for i in range(Niter):
        y = a
        a_next = (a+b)/2
        b = math.sqrt(a*b)
        t -= p * (a-a_next)**2
        a = a_next
        p *= 2
    pi = (a+b)**2 / (4*t)
    return pi

def compute_pi_gauss_legendre_bits(Niter, prec):
    decimal.getcontext().prec = prec

    # Define initial values
    a = decimal.Decimal(1)
    b = decimal.Decimal(1) / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(1) / decimal.Decimal(4)
    p = decimal.Decimal(1)

    for _ in range(Niter):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    return pi

def pi_1k():
    """
    pi con 1000 digitos para usar de referencia
    Referencia: pi con 1000 digitos
    http://www.math.com/tables/constants/pi.htm
    """
    pi1k =('3.1415926535 8979323846 2643383279 5028841971 6939937510'
             '5820974944 5923078164 0628620899 8628034825 3421170679'
             '8214808651 3282306647 0938446095 5058223172 5359408128'
             '4811174502 8410270193 8521105559 6446229489 5493038196'
             '4428810975 6659334461 2847564823 3786783165 2712019091'
             '4564856692 3460348610 4543266482 1339360726 0249141273'
             '7245870066 0631558817 4881520920 9628292540 9171536436'
             '7892590360 0113305305 4882046652 1384146951 9415116094'
             '3305727036 5759591953 0921861173 8193261179 3105118548'
             '0744623799 6274956735 1885752724 8912279381 8301194912'
             '9833673362 4406566430 8602139494 6395224737 1907021798'
             '6094370277 0539217176 2931767523 8467481846 7669405132'
             '0005681271 4526356082 7785771342 7577896091 7363717872'
             '1468440901 2249534301 4654958537 1050792279 6892589235'
             '4201995611 2129021960 8640344181 5981362977 4771309960'
             '5187072113 4999999837 2978049951 0597317328 1609631859'
             '5024459455 3469083026 4252230825 3344685035 2619311881'
             '7101000313 7838752886 5875332083 8142061717 7669147303'
             '5982534904 2875546873 1159562863 8823537875 9375195778'
             '1857780532 1712268066 1300192787 6611195909 2164201989')
    pi1k = pi1k.replace(' ', '')
    return pi1k

