def Del(n,m):
    return n % m == 0
for A in range(1,100_000):
    for x in range(1,100_00):
        if (Del(A,4) and( (not Del(2025,A)) <=(Del(x,1111) <= Del(2024,A))))==0:
            break

    else:
        # если подошло для всех переборов x и не ебнуло
        print(A)