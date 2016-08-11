import math


def calculate_primes(n):
    """
    Calculate the first n prime numbers.

    :param n: The number of prime numbers to calculate
    :return: A list consisting of the first n prime numbers
    """
    primes = []
    i = 2
    while len(primes) < n:
        is_prime = True
        maximum_number = int(math.floor(math.sqrt(i)))
        for prime in primes:
            if prime <= maximum_number and i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes += [i]
        i += 1
    return primes


def find_prime_factors(n):
    """
    Given an integer n, find all its prime factors.

    :param n: An integer
    :return: Prime numbers p_1, ..., p_k such that p_1 * ... * p_k = n
    """
    factors = []
    current_number = n
    current_divisor = 2
    while current_number > 1:
        while current_number % current_divisor == 0:
            current_number /= current_divisor
            factors += [current_divisor]
        current_divisor += 1
    return factors
