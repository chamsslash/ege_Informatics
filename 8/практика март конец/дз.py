from  itertools import *
# num=0
# for i in sorted(product('пейзаж',repeat=5)):
#     num+=1
#     s=''.join(i)
#     if s[0]!='п' and s.count('ж')==3 and s.count('A')<=2:
#         print(num)
#
# num=0
# cnt=0
# for i in sorted(product('термины',repeat=5)):
#     s=''.join(i)
#     num+=1
#     if (((num%2)!=0) and (s[0]!='р' )and (1<=s.count('м')<=2)):
#         cnt+=1
# print(cnt)
# num=0
# cnt=0
# for i in sorted(product('вебинар',repeat=6)):
#     s=''.join(i)
#     num+=1
#     if (((num%2)==0) and (s[0]!='е') and (s.count('р')==2)):
#         cnt+=1
# print(cnt)
# num=0
# res=[]
# for i in sorted(product('крыша',repeat=7)):
#     s=''.join(i)
#     num+=1
#     if (( (num%2)==0) and (s[0]!='ы') and (s.count('ш')==3)):
#         res.append(num)
# print(max(res))
# num=0
# res=[]
# for i in sorted(product('юпитер',repeat=5)):
#     s=''.join(i)
#     num+=1
#     if  (((num%2)!=0) and (s[0]!='р') and (s.count('ю')==2)):
#         res.append(num)
# print(max(res))
# num=0
# o1=0
# o2=0
# for i in product('геэ024',repeat=7):
#     num+=1
#     s=''.join(i)
#     if s=='егэ2024':
#         o1=num
#     if s=='2024егэ':
#         o2=num
# print(max(o1,o2)-min(o1,o2)-1)
num=0
for i in sorted(product('world',repeat=5)):
    s=''.join(i)
    num+=1
    if s[0]=='o':
        print(num)
        break