def print_n_primes(n):
    primes = []
    number = 2
    while len(primes) < n:
        if all(number % prime != 0 for prime in primes):
            primes.append(number)
        number += 1
    return primes

# Example usage
n = 10
prime_list = print_n_primes(n)
print(f"The first {n} prime numbers are:")
print(prime_list)
