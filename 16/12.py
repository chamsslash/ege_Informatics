import sys
from functools import lru_cache
from sys import setrecursionlimit

#
#
# setrecursionlimit(5000)
# @lru_cache(maxsize=None)
# def F(n):
#     if n<6:
#         return n
#     else:
#         return F(n-2)/3+6*n
# for i in range(1,5000):
#     F(i)
# print((F(2234)+3*F(2232))/F(2230))

setrecursionlimit(5000)
# def F(n):
#     if n<50:
#         return n
#     else:
#         return F(n-4)*(n-9)
# for i in range(100_000):
#     F(i)
# print((F(56274)-830*F(56263))//F(56259))
# def F(n):
#     if n<3:
#         return 1
#     if ((n>2) and ((n%2)!=0)):
#         return  F(n-1)+F(n-2)
#     if ((n > 2) and ((n % 2 )== 0)):
#         o1 = sum(F(i) for i in range(1,n))
#         return o1
# for i in range(1,10_00):
#     F(i)
# print(F(28))

# def F(n):
#     if n==5:
#         return n*5
#     if n>5:
#         return  2+F(n-1)+6*G(n-1)
# @lru_cache(maxsize=None)
# def G(n):
#     if n==5:
#         return n*5
#     if n>5:
#         return F(n-1)-G(n-1)+n*G(n-1)
# print(G(18))
#
# def F(n):
#     return 2*(G(n-3)+13)
# @lru_cache(maxsize=None)
# def G(n):
#     if n<6:
#         return 2*n
#     if n>=6:
#         return G(n-2)+3
# for i in range(100_000):
#     G(i)
# print(F(14541))
# @lru_cache(maxsize=None)
# def F(n):
#     if n<=7342:
#         return G(n)
#     if (n>7342 and n%2==0):
#         return F((n//3)-278)+n
#     if (n>7342 and n%2!=0):
#         return F(n-1) +G(n//57)+5
# @lru_cache(maxsize=None)
# def G(n):
#     if n==1:
#         return 1
#     if n>=2:
#         return n*G(n-1)
# for i in range(1,10_000):
#     G(i), F(i)
# # факториал
# # def G(n):
# #     res=1
# #     for o in range(2,n+1):
# #         res*=o
# #     return res
# sys.set_int_max_str_digits(100000)
# print(sum(int(w) for w in str(F(982134) + G(241))))
F=[0]*400_000
for n in range(1,400_000):
    if n==1:
        F[n]=1
    else:
        F[n]=2*n+F[n-1]
print(F[345678])
