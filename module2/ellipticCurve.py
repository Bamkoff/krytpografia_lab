from module1 import randomElement
from module1 import fermatTest
from module1 import effectivePower
from module1 import checkIfRestSquared
from module1 import reverseElement
import random


def generate_prime_number(bits: int):
    p = 4 * randomElement.gen_number_alt(bits) + 3
    while not fermatTest.fermat_test(p):
        p = 4 * randomElement.gen_number_alt(bits) + 3
    return p


def generate_elliptic_curve(p: int):
    A = random.randint(0, p-1)
    # A = 239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159  # test
    B = random.randint(0, p-1)
    # B = 447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221  # test
    delta = 4 * effectivePower.effective_power(A, 3, p) + 27 * effectivePower.effective_power(B, 2, p)
    # print(delta % p)  # test
    while delta % p == 0:
        A = random.randint(0, p)
        B = random.randint(0, p)
        delta = 4 * effectivePower.effective_power(A, 3, p) + 27 * (B, 2, p)
    return A, B, p


def generate_point_on_curve(A, B, p):
    x = random.randint(0, p-1)
    f_x = (effectivePower.effective_power(x, 3, p) + A * x + B) % p
    while not checkIfRestSquared.check_if_rest_squared(f_x, p):
        x = random.randint(0, p - 1)
        f_x = (effectivePower.effective_power(x, 3, p) + A * x + B) % p
    for y in range(0, p):
        if effectivePower.effective_power(y, 2, p) == f_x:
            return x, y
    return None, None


def check_if_point_belongs_to_curve(x, y, A, B, p):
    if effectivePower.effective_power(y, 2, p) == (effectivePower.effective_power(x, 3, p) + A * x + B) % p:
        return True
    else:
        return False


def opposed_point(x, y, p):
    return x, p-y


def sum_points(x1: int, y1: int, x2: int, y2: int, A: int, B: int, p: int):
    if (x1, y1) == opposed_point(x2, y2, p):
        return None, None
    elif x1 == x2 and y1 == y2:
        fi = ((3 * effectivePower.effective_power(x1, 2, p) + A) * reverseElement.reverse_element(p, (2*y1) % p)) % p
        x3 = (effectivePower.effective_power(fi, 2, p) - 2*x1) % p
        return x3, (fi * (x1 - x3) - y1) % p
    else:
        fi = ((y2 - y1) * reverseElement.reverse_element(p, (x2 - x1) % p)) % p
        x3 = (effectivePower.effective_power(fi, 2, p) - x1 - x2) % p
        return x3, (fi * (x1 - x3) - y1) % p