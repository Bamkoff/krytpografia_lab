import math
import random


def find_b(a, p):
    if p % 4 == 3:
        b = 0
        if check_if_rest_squared(a, p):
            b = effective_power(a, int((p + 1) // 4), p)
            return b, p - b
    return None, None


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


def message_into_point(M, A, B, p):
    N = random.randint(1, int(0.05 * p)) + M
    mi = random.randint(1, p // N)
    print(
        "N = ", N,
        "\nmi = ", mi,
    )
    if N * mi < p:
        Mmi = M * mi
        for j in range(1, mi + 1):
            x = Mmi + j
            x = x % p
            f = effective_power(x, 3, p) + A * x + B
            f = f % p
            if check_if_rest_squared(f, p):
                y1, y2 = find_b(f, p)
                if y1 > 0:
                    return x, y1, mi
                else:
                    return x, y2, mi
    return None, None, None


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
        delta = 4 * effective_power(A, 3, p) + 27 * (B, 2, p)
    return A, B, p


def generate_point_on_curve(A, B, p):
    x = random.randint(0, p-1)
    # x = 285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850 # test
    f_x = (effective_power(x, 3, p) + A * x + B) % p
    # print("f_x = ", f_x)
    while not check_if_rest_squared(f_x, p):
        x = random.randint(0, p-1)
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


def generate_keys(k: int, adds=True):
    prime_number = generate_prime_number(k)
    A, B, p = generate_elliptic_curve(prime_number)
    x_p, y_p = generate_point_on_curve(A, B, p)
    x = random.randint(1, int(p+1-2*math.sqrt(p)))
    x_q, y_q = multiple_point(x_p, y_p, x, A, B, p)
    if adds:
        print("K_A = [\n\tE = [\n\t\t A =", A, "\n\t\t B =", B, "\n\t\t]\n\tp =", p, "\n\tP = (\n\t\tx =", x_p,
              "\n\t\ty =", y_p, "\n\t\t)\n\tQ = (\n\t\tx =", x_q,
              "\n\t\ty =", y_q, "\n\t\t)\n\t]")
        print("k_A = [\n\tE = [\n\t\t A =", A, "\n\t\t B =", B, "\n\t\t]\n\tp =", p, "\n\tP = (\n\t\tx =", x_p,
              "\n\t\ty =", y_p, "\n\t\t)\n\tQ = (\n\t\tx =", x_q,
              "\n\t\ty =", y_q, "\n\t\t)\n\tx =", x, "\n\t]")
    return A, B, p, x_p, y_p, x_q, y_q, x


def encode_point(x_pm, y_pm, A, B, p, x_q, y_q, x_p, y_p, adds=True):
    y = random.randint(1, int(p + 1 - 2 * math.sqrt(p)))
    x_c1, y_c1 = multiple_point(x_p, y_p, y, A, B, p)
    x_yq, y_yq = multiple_point(x_q, y_q, y, A, B, p)
    x_c2, y_c2 = sum_points(x_pm, y_pm, x_yq, y_yq, A, B, p)
    if adds:
        print("C1 = (\n", x_c1, "\n", y_c1, "\n)")
        print("C2 = (\n", x_c2, "\n", y_c2, "\n)")
    return x_c1, y_c1, x_c2, y_c2


def decode_c(x_c1, y_c1, x_c2, y_c2, A, B, p, x):
    x_xc1, y_xc1 = multiple_point(x_c1, y_c1, x, A, B, p)
    x_xc1, y_xc1 = opposed_point(x_xc1, y_xc1, p)
    return sum_points(x_c2, y_c2, x_xc1, y_xc1, A, B, p)


def decode_message(x_pm, y_pm, mi):
    return (x_pm - 1) // mi


M = 12345123451234512345123451234512345123451234512345


# A, B, p, x_p, y_p, x_q, y_q, x = generate_keys(300)


# Pm_x, Pm_y, mi = message_into_point(M,
#                           A,
#                           B,
#                           p)
#
# while Pm_x is None or Pm_y is None:
#     Pm_x, Pm_y, mi = message_into_point(M,
#                               A,
#                               B,
#                               p)

p = 2158308180012585622517962433159277509226865987575820766200180666338503937117628551710321171
A = 1836731722933602735158343554244683913046089555652230051394444964369777103984783990620050828
B = 2076220596673757589285054976671455556584365434670303907335216139224820383802089825333393394

x_p = 1850353237444648374538566418033232783862457258945576168429651207613635853543890861853375786
y_p = 313829293586189988264199615074202162038748533609639418153711578560144328326058099419773742

Pm_x = 722038391105641004103161962582784912905702997414284667910565095000982722623537480466108447
Pm_y = 622032669620972825155341407254231315193373792904055537875113985710288682634460353621399021

x = 770635502643446335295032580436928270829182991709203388492525992079871920029

print("Pm = (\n", Pm_x, "\n", Pm_y, "\n)")

x_q, y_q = multiple_point(x_p, y_p, x, A, B, p)

print("Qx = (\n", x_q, "\n", y_q, "\n)")

c1_x, c1_y, c2_x, c2_y = encode_point(Pm_x, Pm_y, A, B, p, x_q, y_q, x_p, y_p, False)

decoded_x, decoded_y = decode_c(c1_x, c1_y, c2_x, c2_y, A, B, p, x)

x_q, y_q = multiple_point(x_p, y_p, x, A, B, p)

print("Pm = (\n", decoded_x, "\n", decoded_y, "\n)")

#print(decode_message(decoded_x, decoded_y, mi) == M)
