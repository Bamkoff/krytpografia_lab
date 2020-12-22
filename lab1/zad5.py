# Zaimplementuj algorytm (funkcję), który oblicza pierwiastek kwadratowy w ciele F∗p,
# gdzie p≡3(mod 4) jest liczbą pierwszą. Wykorzystaj twierdzenie Eulera.
# Dane: a∈F∗p, b jest resztą kwadratową F∗p
# Wynik: a∈F∗p taki, że a^2=b


def effective_power(b: int, k: int, n: int):
    y = 1
    binary = list(reversed(bin(k)[2:]))
    i = len(binary) - 1
    while i >= 0:
        y = (y ** 2) % n
        if binary[i] == "1":
            y = (y * b) % n
        i = i - 1
    return y


def check_if_rest_squared(a, p):
    temp = effective_power(a, int((p-1)/2), p)
    if(temp == 1):
        return True
    else:
        return False


def find_b(a, p):
    if p % 4 == 3:
        b = 0
        if check_if_rest_squared(a, p) == True:
            b = effective_power(a, int((p + 1)//4), p)
            return b, p - b


# print(find_b(23, 59))
# print(find_b(60, 103))
