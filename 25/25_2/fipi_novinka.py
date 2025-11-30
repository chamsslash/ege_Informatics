# My sposob

# import math
#
#
# def free(n):
#     if n<=0: return -1
#     ex=round(math.log(n,3))
#     if 3**ex == n:
#         return ex
#     return -1
#
#
# for shesterki in range(100_000,999_999+1):
#     if str(shesterki).count('1') == 0:
#         for bob in range(1,shesterki):
#             sec=shesterki-bob
#             eshe=free(sec)
#             if  bob%2!=0 and bob%103==0 and eshe>=0:
#                 print(shesterki,eshe

#
# 200004 4
# 200034 6
# 200036 9
# 200050 7
# 200056 10

# Vika's sposob
a=[]
for i in range (1,13):
    for j in  range(1,10_000,2):
        x=3**i+103*j
        if len(str(x)) == 6 and '1' not in str(x):
            a.append([x,i])
print(sorted(a)[:5])