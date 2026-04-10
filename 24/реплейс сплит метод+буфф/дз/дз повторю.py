f=open("Задание 1.txt")
n=f.readline().replace('-',"*").strip().split('*')
maxi=''
buffer=''
for part in n:
    if len(part)!=0 and part[0]!='0':
        buffer+=part+"*"
    elif len(part)!=0 and part[0]=='0' and int(part)!=0:
        buffer=str(int(part))+'*'

    else:
        buffer=''
    maxi = max(buffer, maxi, key=len)
print(len(maxi)-1)