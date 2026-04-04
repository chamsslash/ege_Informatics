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

count = 0
i = 3_000_001

results = []

while count < 5:
    for d in range(2, int(math.sqrt(i)) + 1):
        if i % d == 0:
            other = i // d
            if is_prime(d) and is_prime(other) and has_1_or_3(d) and has_1_or_3(other):
                count += 1
                results.append((i, d, other))
                print(f"#{count}: {i} = {d} * {other}, max factor = {max(d, other)}")
            break
    i += 1

print()
print(f"5th number: {results[4][0]}")
print(f"Largest factor of 5th number: {max(results[4][1], results[4][2])}")
print()
print(f"Answer: {results[4][0]} {max(results[4][1], results[4][2])}")
