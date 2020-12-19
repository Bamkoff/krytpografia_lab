from module1 import randomElement
from module1 import reverseElement
from module1 import effectivePower
from module1 import checkIfRestSquared
from module1 import squareRootInBody
from module1 import fermatTest

# ------ task 1 ------- task 1 -------- task 1 ------ task 1 ------
# Zaimplementuj algorytm (funkcję),
# która generuje losowy element zbioru Zn.
# Dane:k∈N
# Wynik:k-bitowa liczbab∈Zn

print(randomElement.gen_number_alt(100000))

# ------ task 2 ------- task 2 -------- task 2 ------ task 2 ------
# Zaimplementuj algorytm (funkcję) obliczania odwrotności w grupie Φ(n).
# Wykorzystaj Rozszerzony Algorytm Euklidesa.
# Dane:n∈N,b∈Φ(n)
# Wynik:b−1∈Φ(n)

print(reverseElement.reverse_element(7, 6))
# print(reverseElement.reverse_element(714755753874294038472209875197470925790136955101537013834219803636515470795970872969183311384954013071855887627551449115792103595652278095914694551617362804215913432499413006687751873350515301081416609629081600732876172535569616947567263322860053950652618941030441551668294058973216806874984428266145117014661441900618686656150850748874921422072983047618094573078768832033763010726583638946250429569256391196014173690393150623958597147391275931411716442455737215316898025573901638987527999732402901435650871708957843731545984056732362097484684219331952445765843679816824939076287321146124029513354217,
#                       586415287886005945256415364856673789361634830599529970369953159457371797880498621476680842078870442883884206736061308878578202481965828949483342035306607412727247731129489003722107176544339121891058304556107450641845517076214759832220732083103477708296062658308709910111341015680864128408722098158429211163983133076642956241007276594280756931533687913979779606736751482450230516647885181338331851752020358528750514584753773181404184942128231982246579080812899402275455505128052758140697346910131020791692235360755935496686256682912441710402954405191952597983847415248179038414684281386860605203275367))

# ------ task 3 ------- task 3 -------- task 3 ------ task 3 ------
# Zaimplementuj algorytm (funkcję) efektywnego potęgowania w zbiorze Z∗n.
# Wykorzystaj algorytm iterowanego podnoszenia do kwadratu.
# Dane:n, k∈N, b∈Z∗n
# Wynik:bk∈Z∗n

print(effectivePower.effective_power(5, 3, 8))

# ------ task 4 ------- task 4 -------- task 4 ------ task 4 ------
# Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję),
# który sprawdza czy element zbioru Z∗p jest resztą kwadratową wZ∗p.
# Wykorzystaj twierdzenie Eulera.
# Dane: b∈Z∗p
# Wynik: True jeśli b jest resztą kwadratową, False w przeciwnym wypadku.

print(checkIfRestSquared.check_if_rest_squared(26, 13))

# ------ task 5 ------- task 5 -------- task 5 ------ task 5 ------
# Zaimplementuj algorytm (funkcję), który oblicza pierwiastek kwadratowy w ciele F∗p,
# gdzie p≡3(mod 4) jest liczbą pierwszą. Wykorzystaj twierdzenie Eulera.
# Dane: a∈F∗p, b jest resztą kwadratową F∗p
# Wynik: a∈F∗p taki, że a^2=b

print(squareRootInBody.square_root_in_body(23, 59))

# ------ task 6 ------- task 6 -------- task 6 ------ task 6 ------
# Zaimplementuj test (funkcję), który sprawdza czy liczba naturalna jest liczbą pierwszą.
# Wykorzystaj test Fermata
# Dane: n∈N
# Wynik: True jeśli n jest liczbą pierwszą, Falsew przeciwnym wypadku.

print(fermatTest.fermat_test(943923749729479745795479759798579759734597345979578937597359739587398573985793875983759834759735973459873459734985739857359793573598734975983745983745973495734957394579347593847593759734597345973497349857394759347593745934793475973459734957394759374597349573457934759347597345973459734957394579379579579374597359735975173))
