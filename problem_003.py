"""Largest Prime Factor.


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def get_divisors(n: int = 15):
    # assert n > 1; "Integer must be greater than or equal to '2'"
    divisors = []
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
            i += 1
        else:
            i += 1

    return divisors


def _is_divisible_by_any(n: int, integers: list):
    for i in integers:
        if n != i and n % i == 0:
            return True
        else:
            return False


def get_primes(n: int = 20):
    divisors = get_divisors(n)
    primes = []
    for d in divisors:
        if not _is_divisible_by_any(d, divisors):
            primes.append(d)

    return primes


print(max(get_primes(600851475143)))
