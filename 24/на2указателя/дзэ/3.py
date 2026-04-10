f=open('Задание 3.txt')
data= f.readline()[::-1]
res=[]
for i in range(len(data)):
    cnt=0
    if data[i]=='H':
        for j in range(i+1,len(data)):
            if data[j]=='H':
                break
            if data[j] in '13579':
                cnt+=1
            if cnt==34:
                res.append(len(data[i:j+1]))
            if cnt>34:
                break
print(max(res))