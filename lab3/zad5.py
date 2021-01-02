# Zaimplementuj algorytm deszyfrowania ElGamala na krzywej eliptycznej.
# Dane: C= [C1, C2]PM, KA= [E= [A, B, p], p, x, Q, P] - tajny
# Wynik: PM= (x, y)∈E(Fp)



def effective_power(b, k, n):
    y = 1
    binary = list(reversed(bin(k)[2:]))
    i = len(binary) - 1
    while i >= 0:
        y = (y ** 2) % n
        if binary[i] == "1":
            y = (y * b) % n
        i = i - 1
    return y


def reverse_element(n, b):
    A = n
    B = b
    U = 0
    V = 1
    while B != 0:
        q = A // B
        temp = A
        A = B
        B = temp + (-q * B)
        temp = U
        U = V
        V = temp + (-q * V)
    if U < 0:
        return n + U
    return U


def opposed_point(x, y, p):
    return x, p-y


def sum_points(x1: int, y1: int, x2: int, y2: int, A: int, B: int, p: int):
    if (x1, y1) == opposed_point(x2, y2, p):
        return None, None
    elif x1 is None and y1 is None:
        return x2, y2
    elif x2 is None and y2 is None:
        return x1, y1
    elif x1 == x2 and y1 == y2:
        fi = ((3 * effective_power(x1, 2, p) + A) * reverse_element(p, (2*y1) % p)) % p
        x3 = (effective_power(fi, 2, p) - 2*x1) % p
        return x3, (fi * (x1 - x3) - y1) % p
    else:
        fi = ((y2 - y1) * reverse_element(p, (x2 - x1) % p)) % p
        x3 = (effective_power(fi, 2, p) - x1 - x2) % p
        return x3, (fi * (x1 - x3) - y1) % p


def multiple_point(x, y, n, a, b, p):
    N = n
    x_q = x
    y_q = y
    x_r = None
    y_r = None
    while N > 0:
        if N % 2 == 1:
            x_r, y_r = sum_points(x_r, y_r, x_q, y_q, a, b, p)
            N = N - 1
        else:
            x_q, y_q = sum_points(x_q, y_q, x_q, y_q, a, b, p)
            N = N // 2
    return x_r, y_r


def decode_c(x_c1, y_c1, x_c2, y_c2, A, B, p, x):
    x_xc1, y_xc1 = multiple_point(x_c1, y_c1, x, A, B, p)
    x_xc1, y_xc1 = opposed_point(x_xc1, y_xc1, p)
    return sum_points(x_c2, y_c2, x_xc1, y_xc1, A, B, p)


print(decode_c(3801408038035483891687048974661217143464707280667020277954596345515017882569724311659025,
               3166286592509596362097970704229927192809922329639449816252656796669956109713202627620445,
               12375572704791188893273134467942452144929666676976315210466024710454758544393989360122561,
               12087312523582875804495768011251808944929864685937383719058548447992788206355178849753813,
               29709474828707888605740931202360551565636732792371437120940930181130829730156441891744624,
               16643302912691321678918065638057012771154811969628502357120229869058194582706473112319932,
               31338370143412379918310946660817131347405340534853228467935612450555934075843362818014391,
               30522600394850359276797965801607800013346792425205967505486741975047388827950515851621210
))

# c1 = ( 3801408038035483891687048974661217143464707280667020277954596345515017882569724311659025,
#        3166286592509596362097970704229927192809922329639449816252656796669956109713202627620445
#        )
# c2 = ( 12375572704791188893273134467942452144929666676976315210466024710454758544393989360122561,
#        12087312523582875804495768011251808944929864685937383719058548447992788206355178849753813
#        )
