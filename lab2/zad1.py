# Zaimplementuj algorytm (funkcję), która generuje losową krzywą eliptyczną nad Fp.
# Dane: p=3 (mod 4) duża liczba pierwsza (ok. 300 bitów)
# Wynik: A,B ∈ Fp takie, że E:Y2=X3+AX+B jest krzywą nad Fp
from module1 import effectivePower
import random


def fermat_test(x):
    return effectivePower.effective_power(2, x-1, x) == 1


def gen_number_alt(k):
    s = 0
    multiply_by = 1
    i = 0
    while i < k:
        s += random.choice([0, 1]) * multiply_by
        multiply_by = multiply_by * 2
        i += 1
    return s


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


def generate_prime_number(bits: int):
    p = 4 * gen_number_alt(bits) + 3
    while not fermat_test(p):
        p = 4 * gen_number_alt(bits) + 3
    return p


def generate_elliptic_curve(p: int):
    A = random.randint(0, p-1)
    # A = 239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159  # test
    B = random.randint(0, p-1)
    # B = 447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221  # test
    delta = 4 * effective_power(A, 3, p) + 27 * effective_power(B, 2, p)
    # print(delta % p)  # test
    while delta % p == 0:
        A = random.randint(0, p)
        B = random.randint(0, p)
        delta = 4 * effective_power(A, 3, p) + 27 * (B, 2, p)
    return A, B, p


print(generate_elliptic_curve(generate_prime_number(300)))
# print(generate_elliptic_curve(1183779584357076950937981497685946292711107412152534481102525547387604378262522402526266939))  # test
# print(generate_elliptic_curve(11))

# A = 3951502613668786427508319038807867040712174447869623952933414625226341100441832932481097361
# B = 3224696620918517361434419666603980511362432444220251166308109762688821389727537860336481646
# p = 4780750005034460926387212098221027725656916132929395258166013370241258731572975472324340707
