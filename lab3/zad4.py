# Zaimplementuj algorytm szyfrowania ElGamala na krzywej eliptycznej.
# Dane: PM, KA= [E= [A, B, p], p, Q, P], - klucz publiczny
# Wynik: C= [C1, C2], C1, C2∈E(Fp)


import math
import random


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


def encode_point(x_pm, y_pm, A, B, p, x_q, y_q, x_p, y_p):
    y = random.randint(1, int(p + 1 - 2 * math.sqrt(p)))
    x_c1, y_c1 = multiple_point(x_p, y_p, y, A, B, p)
    x_yq, y_yq = multiple_point(x_q, y_q, y, A, B, p)
    x_c2, y_c2 = sum_points(x_pm, y_pm, x_yq, y_yq, A, B, p)
    return x_c1, y_c1, x_c2, y_c2


print(encode_point(370352,
                   14417356443933993270897911104214664176305625947425928443216873599828501207760759429427154,
                   29709474828707888605740931202360551565636732792371437120940930181130829730156441891744624,
                   16643302912691321678918065638057012771154811969628502357120229869058194582706473112319932,
                   31338370143412379918310946660817131347405340534853228467935612450555934075843362818014391,
                   21720083656656870367448257189114242786563415880520465482286418739685583008238067726266194,
                   2644069807894390155787384486719295976943340118365164697373586635540489953969384268657147,
                   20318404056883532543627023358850632855600525569321715204771631283211488553996097309248614,
                   33988889906847781819777291710892235323960728928507600006177399682326446309188431478570))



