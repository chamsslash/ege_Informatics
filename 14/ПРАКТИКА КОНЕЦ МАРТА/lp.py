from string import printable

# o1=1728**555-66*144**554+77*12**553-3*12**100-441
# alph=printable[:12]
# def to12(n):
#     res=''
#     while n:
#         res+=str(alph[n%12])
#         n//=12
#     return res[::-1]
# o12=to12(o1)
# print(o12)
# print(o12.count('b'))
# alph=printable[:13]
# res=[]
# def to13(n):
#     res=''
#     while n:
#         res+=str(alph[n%13])
#         n//=13
#     return res[::-1]
# for x in range(0,4601):
#     o1=3*13**210+11*13**150-x
#     o13=to13(o1)
#     if o13.count('0')==61:
#         res.append(x)
# print(max(res))
# res=[]
# alpha=printable[:21]
# for x in alpha:
#     o1=int(f'33{x}7',21)+int(f'124{x}{x}855',21)
#     if (o1%20)==0:
#         res.append([x,o1/20])
# print(max(res))

# res=[]
# alph=printable[:23]
# for x in alph:
#     for y in alph:
#         o1=int(f'13{y}{x}9',23)+int(f'22{y}22',23)
#         if (o1%2)!=0:
#             break
#     else:
#         o1_1=int(f'13{6}{x}9',23)+int(f'22622',23)
#
#         res.append([x,o1_1/18])
#
# print(max(res))
# res=[]
# for x in range(1,166):
#     o1=2*166**4+7*166**3+x*166**2+5*166**1+1*166**0
#     o2=x*166**3+4*166**2+4*166**1+0*166**0
#     o3=o1+o2
#     if (o3%137)==0:
#         res.append([x,o3//137])
# res.sort(reverse=True)
# print(res[:5])
# print(max(res))
alph=printable[:25]
# bcdfghklmn13579
print(alph)
o1=825**264+456**123-937**26+756**5+56*2-1024
def to25(n):
    res=''
    while n:
        res+=str(alph[n%25])
        n//=25
    return res[::-1]
o25=to25(o1)
res=sum(o25.count(i) for i in 'bcdfghkljmn13579')
print(res)

