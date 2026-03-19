from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(10**6)
# @lru_cache(maxsize=None)
# def F(n):
#     if n<3:
#         return n
#     if n>=3:
#         return F(n-1)+F(n-2)
# @lru_cache(maxsize=None)
# def G(n):
#     if n==1:
#         return n
#     if n>=2:
#         return n*G(n-1)
# for p in range(150_000):
#     F(p),G(p)
# o1=sum(1 for i in str(abs((F(111_111)-G(111_111))//F(111))))
# print(o1)
cnt=0
def F(n):
    if n<=19:
        return n*n*n+22
    if (n>19 and n%3==0):
        return F(n-4)+F(n-8)
    else:
        return F(n-9)+n+7

for ou in range(1,101):
    if all(ch not in str(F(ou)) for ch in '13579'):
        cnt+=1
print(cnt)
