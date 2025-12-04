def Del(n,m):
    return n%m==0
# for A in range(10_000,0,-1):
#     a_podoshel=True
#     for x in range(1,1_000):
#         if ((Del(x,15)) <=((not(Del(x ,A)))<=(not(Del(x,3)))))==0:
#             a_podoshel=False
#             break
#     if a_podoshel:
#         print(A)
#         break
#
#

for A in range(1,10000):
    a_podoshel=True
    for x in range(1,10000):
        if (Del(x,A)<=((Del(x,24))or(not(Del(x,3)))))==0:
            a_podoshel=False
            break
    if a_podoshel:
        print(A)
        break
