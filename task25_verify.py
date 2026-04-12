import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(math.sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True

def has_1_or_3(n):
    s = str(n)
    return '1' in s or '3' in s

for num, d1, d2 in [
    (3000001, 853, 3517),
    (3000009, 3, 1000003),
    (3000013, 773, 3881),
    (3000023, 13, 230771),
    (3000031, 131, 22901),
]:
    print(f"{num} = {d1} * {d2}")
    print(f"  {d1} prime: {is_prime(d1)}, has 1/3: {has_1_or_3(d1)}")
    print(f"  {d2} prime: {is_prime(d2)}, has 1/3: {has_1_or_3(d2)}")
    print(f"  product check: {d1 * d2 == num}")
    print()
