import random


def gen_number(k):
    s = 0
    for i in range(k):
        s += random.choice([0, 1]) * 2**i
    return s


def gen_number_alt(k):
    s = 0
    multiply_by = 1
    i = 0
    while i < k:
        s += random.choice([0, 1]) * multiply_by
        multiply_by = multiply_by * 2
        i += 1
    return s
