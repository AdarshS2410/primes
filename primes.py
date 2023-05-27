def print_n_primes(n):
    primes = []
    sieve = [True] * (n * n)  # Initialize the sieve with True values
    p = 2
    while len(primes) < n:
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n * n, p):
                sieve[i] = False
        p += 1
    return primes

# Example usage
n = 10
prime_list = print_n_primes(n)
print(f"The first {n} prime numbers are:")
print(prime_list)
