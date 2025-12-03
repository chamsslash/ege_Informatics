def Del(n,m):
    return n%m==0

# for A in range(1,1000):
#     a_podoshel=True
#     for x in range(1,10000):
#         if ((Del(x,A) and Del(x,24))<=Del(x,36))!=1:
#             a_podoshel=False
#             break
#     if a_podoshel:
#         print(A)

# for A in range(1,1000):
#     a_podoshel=True
#     for x in range(1,10000):
#         if ((Del(x,64) and (not(Del(x,24)))) <= (not(Del(x,A)))) == 0 :
#             a_podoshel=False
#             break
#     if a_podoshel :
#         print(A)

for A in range(10000,0,-1):
    a_podoshel=True
    for x in range(1,10000):
        if ((not(Del(x,A))) <= (Del(x,45) <= (not(Del(x,75)))))==0:
            a_podoshel=False
            break
    if a_podoshel:
        print(A)

# 225