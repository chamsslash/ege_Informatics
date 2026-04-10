f=open('Задание 1.txt')
data=f.readline()
res=[]
for i in range(len(data)):
    cnt=0
    if data[i] =='D':
        for j in range(i+1,len(data)):
            if data[j]=='D':
                break
            if data[j] in '02468':
                cnt+=1
            if cnt==16:
                res.append(len(data[i:j+1]))
            if cnt>16:
                break
print(max(res))
