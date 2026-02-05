# import functools
# from sys import setrecursionlimit
#
# setrecursionlimit(10000)
#
#
# def F(n):
#     if n==1:
#         return 1
#     else:
#         return (F(n-1)*n)
#
# print((2026*F(2029)+F(2028))//F(2027))
# spiska=[0]*2030
# for i in range(1,2030):
#     if i ==1:
#         spiska[i]=1
#     else:
#         spiska[i]=spiska[i-1]*i
# print((2026*spiska[2029]+spiska[2028])//spiska[2027])
# print(2029*2028*2026+2028)