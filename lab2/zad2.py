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


def find_b(a, p):
    if p % 4 == 3:
        b = 0
        if check_if_rest_squared(a, p):
            b = effective_power(a, int((p + 1)/4), p)
            return b, p - b


def generate_point_on_curve(A, B, p):
    x = random.randint(0, p-1)
    f_x = (effective_power(x, 3, p) + A * x + B) % p
    while not check_if_rest_squared(f_x, p):
        x = random.randint(0, p - 1)
        f_x = (effective_power(x, 3, p) + A * x + B) % p
    y1, y2 = find_b(f_x, p)
    if y1 >= 0:
        return x, y1
    else:
        return x, y2


print(generate_point_on_curve(6, 0, 11))
print(generate_point_on_curve(7442266114772415030352768976382998406784551432504978717073346489409078922166036576925346586,
                              2466337352720946163558594566878067703721357412568959556793569239002025886656197224980680579,
                              7514235270718539427405383888290348979319584377272418465308674358123575315551817468363473339))
# print(generate_point_on_curve(6, 0, 11))
