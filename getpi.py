import math
from fractions import Fraction
from decimal import Decimal

"""
pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...  -> Leibniz Approximation

"""

def calculatePi(n):
    pi = 0
    sign = 1
    for i in range(n):
        nth_term = Fraction(sign, 2 * i + 1)
        pi += nth_term
        sign = -sign
    return 4 * pi

pi = calculatePi(20000)
decimal_pi = Decimal(pi.numerator)/Decimal(pi.denominator)
print(decimal_pi, type(decimal_pi))

float_pi = float(decimal_pi)
print(float_pi)

input_val = input("Which digit? ")
for i in range(int(input_val)):
    float_pi *= 10
    
print(int(float_pi % 10))