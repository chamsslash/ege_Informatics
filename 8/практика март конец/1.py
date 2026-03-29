from itertools import  *
from os.path import join

# cnt=0
# for i in sorted(product('АТОМ',repeat=4)):
#     cnt+=1
#     s='.'.join(i)
#     if s[0]=='О':
#         print(cnt)
#
# print(cnt)

# num=0
# for i in sorted(product('СОРНЯК',repeat=6)):
#     num+=1
#     s=''.join(i)
#     if (s.count('Я')==2 and s.count('К')<=3):
#         print(num)
#         break
# num=0
# cnt=0
# for i in sorted(product('ИНТЕГРАЛ',repeat=5)):
#     s=''.join(i)
#     num+=1
#     if (((num%2)!=0) and (s[0]!='Т') and  (1<=s.count('Н')<=2)):
#         cnt+=1
#
# print(cnt)
# n=0
# cnt=0
# for i in sorted(product('фаворит',repeat=6)):
#     n+=1
#     s=''.join(i)
#     if ((n%2==0) and( s[0]!='о' )and (s.count('р')==2)):
#         cnt+=1
# print(cnt)
# n=0
# cnt=0
# for i in sorted(product(('МОСКВА'),repeat=6)):
#     n+=1
#     s=''.join(i)
#     if (((n%2)==0) and (s[0] not in ['А','В','К']) and (s.count('К')==2) and (s.count('КК')==0)):
#         print(n)
#         break
num=0
for i in sorted(product('СТРЕЛА',repeat=5)):
    s=''.join(i)
    num+=1
    if(( (num%2)==0) and (s.count('Л')==2) and (s.count('ЛЛ') ==0) and (s[0] not in ['А','С','Т'])):
        print(num)
        




