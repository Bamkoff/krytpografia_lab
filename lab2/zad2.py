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
            b = effective_power(a, int((p + 1)//4), p)
            return b, p - b


def generate_point_on_curve(A, B, p):
    x = random.randint(0, p-1)
    # x = 285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850 # test
    f_x = (effective_power(x, 3, p) + A * x + B) % p
    # print("f_x = ", f_x)
    while not check_if_rest_squared(f_x, p):
        x = random.randint(0, p - 1)
        f_x = (effective_power(x, 3, p) + A * x + B) % p
        # print("f_x = ", f_x)
    y1, y2 = find_b(f_x, p)
#    print("y1 = ", y1, ", y2 = ", y2)
    if y1 >= 0:
        return x, y1
    else:
        return x, y2


print("P = ", generate_point_on_curve(6, 0, 11))
print("P = ", generate_point_on_curve(
    3951502613668786427508319038807867040712174447869623952933414625226341100441832932481097361,
    3224696620918517361434419666603980511362432444220251166308109762688821389727537860336481646,
    4780750005034460926387212098221027725656916132929395258166013370241258731572975472324340707))

# print(generate_point_on_curve(6, 0, 11))

# x = 3224560530800846681010680122085616342105068103976973437923049252616388441908964303205172986
# y = 3868781278576523491772112942080376762195328540424175402448760021674499319725602158729657976
