list=[i for i in range(1,101)]
print(list)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

print(" ")
prime_numbers = [n for n in range(1, 101) if is_prime(n)]
print(prime_numbers)