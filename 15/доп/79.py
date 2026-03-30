# q=[i/10 for i in range(260,511)]
# p=[i/10 for i in range(100,351)]
# a=[]
# for x in range(1,10_000):
#     x=x/10
#     o=(((x in p)<=(not(x in q))) or (x in a))
#     if not(o):
#         a.append(x)
# print(a)
# # print(len(a)-1)
# def Del(n,m):
#     return n%m==0
# d=[i for i in range(30,45)]
# for a in range(1,10_000):
#     for x in range(1,10_000):
#
#         if ((not(Del(x,6)) and x not in [45,50,55,60])<= ((abs(x-15)<=5)<=(x in d)) or ( x&a!=0))==0:
#             break
#     else:
#         print(a)

U = set(range(11249, 200491 + 1))
M = set(range(11252, 200493 + 1))
S = set(range(11252, 200494 + 1))
C = set(range(11254, 200489 + 1))
O = set(range(11251, 200490 + 1))
L=[
]
for x in range(200900,10000,-1):

    form= (((x in U) and (x in M)) and ((x in S) or (x in C) and (x in O)))
    if  form:
        L.append(x)
ww
print(L[0]-L[-1])

