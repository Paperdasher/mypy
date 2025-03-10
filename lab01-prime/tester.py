## Lab01 TESTER ##

from prime import is_prime
from prime import nthPrime


def isPrimeC(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nthPrime(n):
    count = 0
    i = 2
    while count < n:
        if isPrimeC(i):
            count += 1
        i += 1
    return i - 1


print("Testing is_prime()")
for i in range(0, 100):
    if isPrimeC(i) != is_prime(i):
        print("is_prime() failed on input: ", i)
        break



print("Testing nthPrime()")

for i in range(0, 100):
    if nthPrime(i) != nthPrime(i):
        print("nthPrime() failed on input: ", i)
        break