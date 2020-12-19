# Zaimplementuj algorytm (funkcję),
# która generuje losowy element zbioru Zn.
# Dane:k∈N
# Wynik:k-bitowa liczbab∈Zn

import random


def gen_number(k):
    sum = 0
    for i in range(k):
        sum += random.choice([0, 1]) * 2**i
    return sum


def gen_number_alt(k):
    sum = 0
    multiply_by = 1
    i = 0
    while i < k:
        sum += random.choice([0, 1]) * multiply_by
        multiply_by = multiply_by * 2
        i += 1
    return sum


print(gen_number_alt(100000))
