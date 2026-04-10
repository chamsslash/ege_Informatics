f=open('Задание 2.txt')
data=f.readline()
res=[]
for i in range(len(data)):
    k=0
    if data[i]=='R':
        for j in range(i+1,len(data)):
            if data[j]=='R':
                break
            if data[j] in '13579':
                k+=1
            if k == 23:
                res.append(len(data[i:j + 1]))
            if k>23:
                break

print(max(res))