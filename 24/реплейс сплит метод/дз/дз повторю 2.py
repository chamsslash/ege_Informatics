f=open('Задание 2.txt')
n=f.readline().strip().replace('-',"*").split('*')
buffer=''
maxi=''
for chunk in n:
    if len(chunk)>0 and chunk[0]!='0':
        buffer+=chunk+'*'
        maxi=max(maxi,buffer,key=len)
    elif len(chunk)>1 and chunk[0]=='0':
        buffer+='0*'
        maxi=max(maxi,chunk,key=len)
        buffer=str(int(chunk))+'*'
        maxi=max(maxi,buffer,key=len)
    elif len(chunk)==1 and chunk[0]=='0':
        buffer+='0*'
        maxi=max(maxi,buffer,key=len)
    else:
        buffer=''
print(maxi)
print(len(maxi)-1)