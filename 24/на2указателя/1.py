f=open('24_1.txt')
data=f.readline()
res=[]
for l in range(len(data)):
    if data[l] =='L':
        cnt=0
        for j in range(l+1,len(data)):
            if data[j]=='L':
                break
            if data[j] in '02468':
                cnt += 1
            if cnt> 14:
                break
            if cnt==14:
                res.append(len(data[l:j+1]))
print(max(res))