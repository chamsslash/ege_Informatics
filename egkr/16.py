# import sys
# from functools import lru_cache
# from sys import setrecursionlimit
# setrecursionlimit(10**6)
# sys.set_int_max_str_digits(10**6)
# @lru_cache(maxsize=None)
# def F(n):
#     if n<10:
#         return 3
#     if n>=10:
#         return (n+4) * F(n-5)
# for uu in range(300_000):
#     F(uu)
# print((F(257_487)//683+67*F(257477))//F(257472))
# решал руками через вынесения
print(257481*(((257491*257486)/683)+67))
# 24994270044009