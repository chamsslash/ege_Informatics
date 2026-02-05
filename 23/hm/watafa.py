# from functools import lru_cache
# from sys import setrecursionlimit
#
# setrecursionlimit(100000)
#
# @lru_cache(None)
# def f(m,n):
#     if m == 0:
#         return n + 1
#     if n == 0:
#         return f(m-1,1)
#     return f(m-1,f(m,n-1))
#
# # прогрев кеша
# for i in range(5):
#     for j in range(100):
#         f(i,j)
#
# print(f(4,1))
