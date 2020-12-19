# Zaimplementuj algorytm (funkcję), który oblicza punkt przeciwny do danego punktu.
# Dane: P=(x, y) ∈ E(Fp)
# Wynik: −P=(x,−y) ∈ E(Fp)


def opposed_point(x, y, p):
    return x, p-y


print(opposed_point(5, 1, 11))
