# Zaimplementuj algorytm generowania kluczy kryptosystemu ElGamala na krzywej elip-tycznej.
# Dane: k liczba bitów p
# Wynik: KA= [E = [A, B, p], p, Q, P],- klucz publiczny, kA= [E= [A, B, p], p, x, Q, P]-klucz tajny, gdzie p= 3 (mod 4), Q, P∈E(Fp)
import random
import math


def check_if_rest_squared(b: int, p: int):
    temp: int = effective_power(b, int((p-1)//2), p)
    if temp == 1:
        return True
    else:
        return False


def find_b(a, p):
    if p % 4 == 3:
        b = 0
        if check_if_rest_squared(a, p):
            b = effective_power(a, int((p + 1)//4), p)
            return b, p - b


def fermat_test(x):
    return effective_power(2, x-1, x) == 1


def gen_number_alt(k):
    s = 0
    multiply_by = 1
    i = 0
    while i < k:
        s += random.choice([0, 1]) * multiply_by
        multiply_by = multiply_by * 2
        i += 1
    return s


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


def generate_prime_number(bits: int):
    p = 4 * gen_number_alt(bits) + 3
    while not fermat_test(p):
        p = 4 * gen_number_alt(bits) + 3
    return p


def check_if_elliptic_curve(A, B, p):
    if (4 * effective_power(A, 3, p) + 27 * effective_power(B, 2, p)) % p == 0:
        return False
    return True


def generate_elliptic_curve(p: int):
    A = random.randint(0, p-1)
    # A = 239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159  # test
    B = random.randint(0, p-1)
    # B = 447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221  # test
    delta = 4 * effective_power(A, 3, p) + 27 * effective_power(B, 2, p)
    # print(delta % p)  # test
    while delta % p == 0:
        A = random.randint(0, p)
        B = random.randint(0, p)
        delta = 4 * effective_power(A, 3, p) + 27 * effective_power(B, 2, p)
    return A, B, p


def generate_point_on_curve(A, B, p):
    x = random.randint(0, p-1)
    # x = 285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850 # test
    f_x = (effective_power(x, 3, p) + A * x + B) % p
    # print("f_x = ", f_x)
    while not check_if_rest_squared(f_x, p):
        x = random.randint(0, p - 1)
        f_x = (effective_power(x, 3, p) + A * x + B) % p
        # print("f_x = ", f_x)
    y1, y2 = find_b(f_x, p)
#    print("y1 = ", y1, ", y2 = ", y2)
    if y1 >= 0:
        return x, y1
    else:
        return x, y2


def opposed_point(x, y, p):
    return x, p-y


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
    x_q = x
    y_q = y
    x_r = None
    y_r = None
    while n > 0:
        if n % 2 == 1:
            x_r, y_r = sum_points(x_r, y_r, x_q, y_q, a, b, p)
            n -= 1
        x_q, y_q = sum_points(x_q, y_q, x_q, y_q, a, b, p)
        n = n // 2
    return x_r, y_r


def generate_keys(k: int):
    prime_number = generate_prime_number(k)
    A, B, p = generate_elliptic_curve(prime_number)
    x_p, y_p = generate_point_on_curve(A, B, p)
    x = random.randint(1, int(p+1-2*math.sqrt(p)))
    x_q, y_q = multiple_point(x_p, y_p, x, A, B, p)
    print("K_A = [\n\tE = [\n\t\t A =", A, "\n\t\t B =", B, "\n\t\t]\n\tp =", p, "\n\tP = (\n\t\tx =", x_p,
          "\n\t\ty =", y_p, "\n\t\t)\n\tQ = (\n\t\tx =", x_q,
          "\n\t\ty =", y_q, "\n\t\t)\n\t]")
    print("k_A = [\n\tE = [\n\t\t A =", A, "\n\t\t B =", B, "\n\t\t]\n\tp =", p, "\n\tP = (\n\t\tx =", x_p,
          "\n\t\ty =", y_p, "\n\t\t)\n\tQ = (\n\t\tx =", x_q,
          "\n\t\ty =", y_q, "\n\t\t)\n\tx =", x, "\n\t]")


generate_keys(300)
