def count_primes(start, end):
    count = 0
    for number in range(start, end + 1):
        if is_prime(number):
            count += 1
    return count

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
start = 1
end = 100
prime_count = count_primes(start, end)
print(f"The number of prime numbers between {start} and {end} is: {prime_count}")
