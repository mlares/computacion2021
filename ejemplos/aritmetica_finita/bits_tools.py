from bitstring import BitArray, BitStream
import struct

BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
MAGENTA = "\033[0;35m"
RESET = "\033[0;0m"


def float_to_bin(x, precision=64, show_construct=False,
              show_compute=False, show_bitstring=False):
    """Transform from float to binary with a given precision

    Alowed values for precision are 8, 16, 32 and 64. Representation 
    follows IEEE 754-2019 standard (see e.g.
    https://standards.ieee.org/standard/754-2019.html).
    This function is part of the course "Computación", FaMAF, 2021

    Parameters
    ----------
    x: float
    precision: int
        8  for quarter precision 1+3+4
        16 for half precision    1+5+10
        32 for single precision  1+8+23
        64 for double precision  1+11+52
    show_construct: bool
        Show a string with the computation of the closest
        representation
    show_compute: bool
        Show a string with the computation of the closest
        representacion, which can be run as it is.
    show_bitstring: bool
        Show the binary representation separating with color the
        sign, exponent and mantissa

    returns
    -------
    rr: string
        a string containing the binary representacion of the number "x"
        with precision "precision", with colors.
    s: string
    e: string
    m: string
    r: string
    """
    if precision==32:
        b = BitArray(float=x, length=32).bin
        s = b[0]
        e = b[1:9]
        m = b[9:]
    elif precision==64:
        b = BitArray(float=x, length=64).bin
        s = b[0]
        e = b[1:12]
        m = b[12:]
    elif precision==16:
        b = BitArray(float=x, length=32).bin
        s = b[0]
        e = b[1] + b[1:9][-4:]
        m = b[9:][:10]
    elif precision==8:
        b = BitArray(float=x, length=32).bin
        s = b[0]
        e = b[1] + b[1:9][-2:]
        m = b[9:][:4]
    else:
        print('Wrong precision value! Try 32 or 64')
        b=s=e=m=''

    n = int(e, 2)
    n = n - 2**(len(e)-1) + 1
    pr = '+ ( 1 ' if s=='0' else '- ( 1 '
    prs = '+ [1 ' if s=='0' else '- [1 '
    prs0 = '+ [1 ' if s=='0' else '- [1 '
    r = 0
    for k, b in enumerate(m):
        f = 0 if b=='0' else 1
        prs0 = prs0 + f'+{f}·½^{k+1}'
        if f:
            pr = pr + f'+ {f} * (1/2)**{k+1} '
            prs = prs + f'+ {f}·(½)^{k+1} '
        r = r + int(f)*(1/2)**(k+1)
    pr = pr + f') * 2**{n} '
    prs = prs + f'] · 2^{n} '
    prs0 = prs0 + f'] · 2^{n} '
    r = (1 + r) * 2**n

    if show_compute:
        print(pr)
        print(f'Número ingresado: {x}, número recuperado: {r}')
        exec(f'print({pr})')
    if show_construct:
        print(prs0)
    if s==1:
        r = -r

    rr = ' '.join([BLUE, s, GREEN, e, CYAN, m, RESET])
    if show_bitstring:
        print(rr)

    return rr, s, e, m, r




# x = 2.11111111
# print(f'Número ingresado: {x}')
# 
# print('\n' + MAGENTA + ' Representación en 64 bits:')
# s, ss, e, m, r = float2bin(x, 64, False)
# print(s)
# print(RESET, '---->', r)
# 
# print('\n' + MAGENTA + ' Representación en 32 bits:')
# s, ss, e, m, r = float2bin(x, 32, False)
# print(s)
# print(RESET, '---->', r)
# 
# print('\n' + MAGENTA + ' Representación en 16 bits:')
# s, ss, e, m, r = float2bin(x, 16, True)
# print(s)
# print(RESET, '---->', r)
# 
# print('\n' + MAGENTA + ' Representación en 8 bits:')
# s, ss, e, m, r = float2bin(x, 8, False)
# print(s)
# print(RESET, '---->', r)


def bin_to_float(bitstring, precision=64):
    """Transform from binary to float
    """
    
    b = bitstring
    if precision==64:
        s = b[0]
        e = b[1:12]
        m = b[12:]
    elif precision==32:
        s = b[0]
        e = b[1:9]
        m = b[9:]
    elif precision==16:
        s = b[0]
        e = b[1] + b[1:9][-4:]
        m = b[9:][:10]
    elif precision==8:
        s = b[0]
        e = b[1:4]
        m = b[4:]

    n = int(e, 2)
    n = n - 2**(len(e)-1) + 1
    r = 0
    for k, b in enumerate(m):
        f = 0 if b=='0' else 1
        r = r + int(f)*(1/2)**(k+1)
    r = (1 + r) * 2**n
    if s==1:
        r = -r
    return r


# def binary(num, prec=8):
#     s = [bin(c).replace('0b', '').rjust(prec, '0') for c in struct.pack('!f', num)]
#     return s
# 
# def binary_str(num):
#     bits = ''.join(binary(num))
#     s = ''.join([BLUE, bits[:1], GREEN, bits[1:10], CYAN, bits[10:],
#  RESET])
#     return s, bits[:1], bits[1:10], bits[10:]
# 
# # 16 bits?
# def binary_str_fp16(num):
#     bits = ''.join(binary(num))
#     s = ''.join([BLUE, bits[:1], GREEN, bits[1:10][-5:], CYAN, bits[10:][:11], RESET])
#     return s, bits[:1], bits[1:10][-5:], bits[10:][:11]
# x = 2.2
# print(x, "as fp32:", binary_str(0.7), "as fp16 is sort of:", binary_str_fp16(0.7))
