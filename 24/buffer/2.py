from string import printable

f=open('24_2.txt')
data=f.readline().strip()
buff=''
def checkup(pod):
    for i in range(len(pod)-1):
        for j in range(i+1,len(pod)):
            o1=pod[i:j+1]
            if ((o1 == o1[::-1]) and ((len(o1)%2)!=0) and ((int(o1[len(o1)//2],18)%2)==0)):
                return o1
    return ''

alph='0123456789ABCDEFGH'
res=[]
for d in data:
    if len(buff)==0 and  d in alph[1:]:
        buff=d
    elif ((len(buff))>0):
        if d in alph:
            buff+=d
        else:
            if checkup(buff)!='':
                res.append(checkup(buff))
            buff=''
print(res)
print(max(res,key=len))
print(len(max(res,key=len)))