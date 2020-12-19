# Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję),
# który sprawdza czy element zbioru Z∗p jest resztą kwadratową w Z∗p.
# Wykorzystaj twierdzenie Eulera.
# Dane: b∈Z∗p
# Wynik: True jeśli b jest resztą kwadratową, False w przeciwnym wypadku.
from module1 import effectivePower


def check_if_rest_squared(b: int, p: int):
    temp: int = effectivePower.effective_power(b, int((p-1)//2), p)
    if temp == 1:
        return True
    else:
        return False


# print(check_if_rest_squared(26, 13))
# print(check_if_rest_squared(3, 13))
# print(check_if_rest_squared(5, 13))
# print(check_if_rest_squared(1, 11))
# print(check_if_rest_squared(646364623469634716329421551581459444393459634563465364563456387456873465873645876345876345876345876345876345863458763458763485763485763487563845638465837465834658765735646345645856346875,
#                             943923749729479745795479759798579759734597345979578937597359739587398573985793875983759834759735973459873459734985739857359793573598734975983745983745973495734957394579347593847593759734597345973497349857394759347593745934793475973459734957394759374597349573457934759347597345973459734957394579379579579374597359735975173))
