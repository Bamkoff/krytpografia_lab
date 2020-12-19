# Zaimplementuj algorytm (funkcję), który znajduje losowy punkt na krzywej eliptycznej nad Fp.
# Dane:A, B, p= 3 (mod 4)takie, że E:Y^2=X^3+AX+B jest krzywą nad Fp
# Wynik:P= (x, y) ∈ E(Fp)
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


def check_if_rest_squared(b: int, p: int):
    temp: int = effective_power(b, int((p-1)//2), p)
    if temp == 1:
        return True
    else:
        return False


def generate_point_on_curve(A, B, p):
    x = random.randint(0, p-1)
    f_x = (effective_power(x, 3, p) + A * x + B) % p
    while not check_if_rest_squared(f_x, p):
        x = random.randint(0, p - 1)
        f_x = (effective_power(x, 3, p) + A * x + B) % p
    for y in range(0, p):
        if effective_power(y, 2, p) == f_x:
            return x, y
    return None, None


print(generate_point_on_curve(6, 0, 11))
# print(generate_point_on_curve(6, 0, 11))
