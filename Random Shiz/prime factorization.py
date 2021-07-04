import math

# A function to print all prime factors of
# a given number n
def primeFactors(n):
    factors = []
    # Print the number of two's that divide n
    if n % 2 == 0:
        factors.append([2, 0])
    while n%2 == 0:
        n = n // 2
        factors[-1][1] += 1

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i ad divide n
        if n%i == 0:
            factors.append([i, 0])
        while n%i == 0:
            n = n // i
            factors[-1][1] += 1

    if n > 2:
        factors.append([n, 1])

    return factors

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b = 420, 364

print(gcd(a, b))