f=open('24_2.txt')
data=f.readline()
res=[]
for l in range(len(data)):
    cnt=0
    if data[l]=='S':
        for j in range(l+1,len(data)):
            if data[j]=='S':
                break
            if data[j] in '13795':
                cnt+=1
            if cnt==35:
                res.append(len(data[l:j+1]))
            if cnt>=35:
                break
print(max(res))