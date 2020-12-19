# Zaimplementuj algorytm (funkcję), który sprawdza czy punkt należy do krzywej.
# Dane:P= (x, y) oraz A, B, p= 3 (mod 4) takie, że E:Y2=X3+AX+B jest krzywą nad Fp
# Wynik: True jeśli P= (x, y) ∈ E(Fp) w przeciwnym przypadku False


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


def check_if_point_belongs_to_curve(x, y, A, B, p):
    if effective_power(y, 2, p) == (effective_power(x, 3, p) + A * x + B) % p:
        return True
    else:
        return False


print(check_if_point_belongs_to_curve(5, 1, 6, 0, 11))
print(check_if_point_belongs_to_curve(7, 1, 6, 0, 11))
