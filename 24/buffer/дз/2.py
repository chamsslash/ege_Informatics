import string


def zerkala(n):
    palids=[]
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            o1=n[i:j+1]
            if (o1==o1[::-1] ) and ((len(o1)%2)!=0) and ((int(o1[len(o1)//2],25)%2)==0) and o1!='0':
                palids.append(o1)
    if len(palids)>0:
        return max(palids,key=len)
    return ''
f=open('Задание 2.txt')
alph=string.digits+string.ascii_uppercase[:15]
data=f.readline().strip()
buff=''
res=[]
for i in data:
    if len(buff)==0 and i in alph[1:]:
        buff=i
    elif len(buff)>0 and i  in alph:
        buff+=i
    else:
        yu=zerkala(buff)
        if yu!='':
            res.append(yu)
        buff=''
res.append(buff)
print(max(res,key=len))
print(len(max(res,key=len)))