# Zaimplementuj test (funkcję), który sprawdza czy liczba naturalna jest liczbą pierwszą.
# Wykorzystaj test Fermata
# Dane: n∈N
# Wynik: True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.


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


def fermat_test(x):
    return effective_power(2, x-1, x) == 1


# print(fermat_test(4))
# print(fermat_test(3))
# print(fermat_test(8))
# print(fermat_test(11))
# print(fermat_test(23))
# print(fermat_test(24))
print(fermat_test(943923749729479745795479759798579759734597345979578937597359739587398573985793875983759834759735973459873459734985739857359793573598734975983745983745973495734957394579347593847593759734597345973497349857394759347593745934793475973459734957394759374597349573457934759347597345973459734957394579379579579374597359735975173))



