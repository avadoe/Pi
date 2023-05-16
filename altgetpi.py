import math

def calculate_pi(n_terms):
    """
    Leibniz Formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    """
    numerator, denominator = 1, 1
    operator, pi = 1, 0
    for i in range(n_terms):
        pi += operator * numerator/denominator
        denominator += 2
        operator = -operator
    return pi * 4

def getNthDigit(n):
    num_terms = int(math.ceil((n + 1)/0.3010299956639812))
    pi_val = calculate_pi(num_terms)
    pi_str = str(pi_val)
    return int(pi_str[n + 1])

n = input("Enter n: ")
print(f"Nth digit of pi is {getNthDigit(int(n))}")