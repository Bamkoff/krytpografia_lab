import random

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

def gen_number_alt(k):
    sum = 0
    multiply_by = 1
    i = 0
    while i < k:
        sum += random.choice([0, 1]) * multiply_by
        multiply_by = multiply_by * 2
        i += 1
    return sum


flag = True
while flag:
    q = gen_number_alt(250)
    while not fermat_test(q):
        q = gen_number_alt(250)
        print(q)
    p = 2*q + 1
    if fermat_test(p):
        flag = False
        print("p = ", p, ", q = ", q)
        g = random.randint(1, p-1)
        pow_g = effective_power(g, q, p)
        print(pow_g)
        while pow_g == 1:
            pow_g = effective_power(g, q, p)
            print(pow_g)
        print("g = ", g)

