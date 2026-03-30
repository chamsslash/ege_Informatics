# def to4(n):
#     res=''
#     while n>0:
#         res+=str(n%4)
#         n=n//4
#
#     return res[::-1]
# o1=[]
# for n in range(1,100_000):
#     n4=to4(n)
#     n4=n4+n4[-3:] if n%3==0 else to4((n%3)*4)+n4
#     r=int(n4,4)
#     if r <1166:
#         o1.append(n)
# print(max(o1))
# import math
# res=[]
#
# for n in range(100,1000):
#     s_n=str(n)
#     umn=math.prod(int(i)for i in s_n)
#     summ=sum(int(i)for i in s_n)
#     o1=str(max(umn,summ))+str(min(umn,summ))
#     if o1 =='6012':
#         res.append(n)
#
# print(max(res))
res=[]
for n in range(1000,10_000):
    s_n=str(n)
    dicks=[int(i)for i in s_n]
    S=sum(dicks)
    M=max(dicks)
    N=min(dicks)
    p1=S-M
    p2=S-N
    O1=str(min(p1,p2))+str(max(p1,p2))
    if O1=='1318':
        res.append(n)
print(min(res))

