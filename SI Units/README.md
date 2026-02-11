 The International System of Units (SI) defines 7 base units: s (second), m (meter), kg (kilogram), A (ampere), K (kelvin), mol (mole) and cd (candela). In addition to base units, there are 22 derived units, which can all be represented as products of powers of these base units.
rad 	1
sr 	1
Hz 	s^-1
N 	kg m s^-2
Pa 	kg m^-1 s^-2
J 	kg m^2 s^-2
W 	kg m^2 s^-3
C 	A s
V 	kg m^2 s^-3 A^-1
F 	kg^-1 m^-2 s^4 A^2
Ω 	kg m^2 s^-3 A^-2
S 	kg^-1 m^-2 s^3 A^2
Wb 	kg m^2 s^-2 A^-1
T 	kg s^-2 A^-1
H 	kg m^2 s^-2 A^-2
°C 	K
lm 	cd
lx 	cd m^-2
Bq 	s^-1
Gy 	m^2 s^-2
Sv 	m^2 s^-2
kat 	mol s^-1

SI also defines 24 symbols known as prefixes, denoting powers of ten.
Q 	10^30
R 	10^27
Y 	10^24
Z 	10^21
E 	10^18
P 	10^15
T 	10^12
G 	10^9
M 	10^6
k 	10^3
h 	10^2
da 	10^1
d 	10^-1
c 	10^-2
m 	10^-3
μ 	10^-6
n 	10^-9
p 	10^-12
f 	10^-15
a 	10^-18
z 	10^-21
y 	10^-24
r 	10^-27
q 	10^-30

Each argument is an SI unit with a possible prefix. Print it as a product of a power of ten and its base units. For example, GW (gigawatt) becomes 10^9 kg m^2 s^-3. Keep in mind the following exceptions:

    The kilogram is a base unit with an inherent prefix. Other prefixes attach to g (gram), and you should print their values relative to the kilogram: g is 10^-3 kg and Mg is 10^3 kg.
    Instead of 10^1, print 10.
    Instead of 10^0, print 1.
    For rad and sr, only print a power of ten. (Example: for Mrad, print 10^6, not 10^6 1.)
    There is no universal order among the base units. For C, you must output A s rather than s A. We follow the conventions of NIST.
    μ is U+03BC GREEK SMALL LETTER MU (UTF-8: ce bc).
    Ω is U+03A9 GREEK CAPITAL LETTER OMEGA (UTF-8: ce a9).
    ° is U+00B0 DEGREE SIGN (UTF-8: c2 b0). 
