# Zaimplementuj algorytm (funkcję), który oblicza pierwiastek kwadratowy w ciele F∗p,
# gdzie p≡3(mod 4) jest liczbą pierwszą. Wykorzystaj twierdzenie Eulera.
# Dane: a∈F∗p, b jest resztą kwadratową F∗p
# Wynik: a∈F∗p taki, że a^2=b
from module1 import checkIfRestSquared


def square_root_in_body(a, p):
    if p % 4 == 3:
        b = 0
        if checkIfRestSquared.check_if_rest_squared(a, p):
            b = checkIfRestSquared.effective_power(a, int((p + 1)//4), p)
            return b, p - b


# print(find_b(23, 59))
# print(find_b(60, 103))
