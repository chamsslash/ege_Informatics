f=open("дз/Задание 2.txt")
a=f.readline()
buff=a[0]
res=[]
for i in range(len(a)-1):
    sum=0
    for symb in buff+str(a[i+1]):
        sum+=int(symb)**(len(buff)+1)
        if sum==int(buff+str(a[i+1])):
            buff+=str(a[i+1])
            res.append(buff)
        else:
            buff=str(a[i+1])
maximum=max(res)
count=res.count(maximum)
print(count)