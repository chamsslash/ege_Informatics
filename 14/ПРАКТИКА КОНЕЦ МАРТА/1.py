from string import printable

# alpha=printable[:11]
# def to11(n):
#     res=''
#     while n:
#         res+=str(alpha[n%11])
#         n//=11
#     return res[::-1]
# o1=1331**650-55*121**610+77*11**510-3*11**100-221
# o11=to11(o1)
# print(o11)
# r=o11.count('a')
# print(r)
#
# alpha=printable[:28]
# def toebat(n):
#     res=''
#     while n:
#         res+=str(alpha[n%27])
#         n//=27
#     return res[::-1]
# o=3*2187**2020+3*729**2021-2*81**2022 +27**2023 -4*3**2024-2029
# o27=toebat(o)
# print(o27)
# u=sum(o27.count(i) for i in printable[10:28])
# print(u)
# alpha=printable[:50]
# def to49(n):
#     res=''
#     while n:
#         res+=str(alpha[n%49])
#         n//=49
#     return res[::-1]
# o1=2*2401**525+3*343**524-4*49**523+5*49**522-6*7**521-35
# o49=to49(o1)
# print(o49)
# iu=sum(o49.count(i) for i in printable[:10])
# print(iu)
# alpha=printable[:4]
# off=[]
# def to3(n):
#     res=''
#     while n:
#         res+=str(alpha[n%3])
#         n//=3
#     return res[::-1]
# for x in range(0,2031):
#     o1=3**100-x
#     o3=to3(o1)
#     if o3.count('0')==5:
#         off.append(x)
# print(max(off))

# alpha=printable[:27]
# res=[]
# def toebat(n):
#     res=''
#     while n:
#         res+=str(alpha[n%27])
#         n//=27
#     return res[::-1]
# for x in range(0,27001):
#     o1=3*27**9+2*27**6+27**3 -x
#     o27=toebat(o1)
#     if o27.count('0')==6:
#         res.append(x)
# print(min(res))


# res=[]
# alpha=printable[:21]
# for x in alpha:
#     o1=int(f'82934{x}2',21)+int(f'2924{x}{x}7',21)+int(f'67564{x}8',21)
#     if ((o1%20)==0):
#         res.append([x,o1/20])
# res.sort()
# print(res[:5])
# print(min(res))



# alpha=printable[:26]
# res=[]
#
# for x  in alpha:
#     for y in alpha:
#         o1=int(f'13{y}{x}5',26)+int(f'24{y}13',26)
#         if (o1%8)!=0:
#             break
#     else:
#         o1_1=int(f'132{x}5',26)+int(f'24213',26)
#         res.append([x,o1_1/8])
# res.sort(reverse=True)
# print(res[:5])
# print(max(res))
#
# res=[]
# for x in range(1,150):
#     o1=5*150**4+1*150**3+x*150**2+2*150**1+9*150**0
#     o2=x*150**3+0*150**2+2*150**1+3*150**0
#     o3=o1+o2
#     if (o3%149)==0:
#         res.append([x,o3/149])
# res.sort(reverse=True)
# print(res[:5])
# print(max(res))

# res=[]
# for x in range(0,40):
#     o1=8*40**6+7*40**5+1*40**4+x*40**3+2*40**2+9*40**1+1*40**0
#     o2=3*40**6+6*40**5+6*40**4+x*40**3+6*40**2+3*40**1+1*40**0
#     o3=9*40**6+7*40**5+3*40**4+x*40**3+6*40**2+1*40**1+8*40**0
#     o4=o1+o2+o3
#     if (o4%39)==0:
#         res.append([x,o4/13])
# res.sort()
# print(res[:5])
# print(min(res))
res=[]
alpha=printable[:29]
for x in alpha:
    o1=int(f'923{x}874',29)+int(f'524{x}6152',29)
    if (o1%28)==0:
        res.append([x,o1/28])
res.sort(reverse=True)
print(res[:5])
print(max(res))