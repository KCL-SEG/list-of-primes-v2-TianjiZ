"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(number):
    """Determine if a number is a prime number."""
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def primes(count):
    """Generate a list of prime numbers up to the specified count."""
    if count <= 0:
        raise ValueError("The count must be a positive integer")

    prime_numbers = []
    current_number = 2
    while len(prime_numbers) < count:
        if check_prime(current_number):
            prime_numbers.append(current_number)
        current_number += 1

    return prime_numbers

