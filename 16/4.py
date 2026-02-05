from functools import lru_cache
from sys import setrecursionlimit


# setrecursionlimit(10_000)
#
# @lru_cache(None)
#
# def F(n):
#     return 3*G(n-3)+11
# @lru_cache(None)
# def G(n):
#     if n<12:return 5*n
#     else: return G(n-4)+7
#
#
# for i in range(0,20_001):
#     F(i)
# print(F(20001))
# f=[0]*30_000
# g=[0]*30_000
#
# for i in range(20_002):
#     if i<12:g[i]=5*i
#     else:g[i]=g[i-4]+7
# for n in range(3,30_000):
#     f[n]=3*g[n-3]+11
# print(f[20001])
# N = 50000
# G_vals = [0] * (N + 1)
# F_vals = [0] * (N + 1)
#
# for n in range(N + 1):
#     if n < 12:
#         G_vals[n] = 5 * n
#     else:
#         G_vals[n] = G_vals[n - 4] + 7
#
# for n in range(3, N + 1):
#     F_vals[n] = 3 * G_vals[n - 3] + 11
#
# print(F_vals[20001])
