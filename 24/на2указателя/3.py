f=open('24_3.txt')
data=f.readline()[::-1]
res=[]
for i in range(len(data)):
    cnt=0
    if data[i]=='K':
     for j in range(i+1,len(data)):
         if data[j] in '13579':
             cnt+=1
         if data[j]=='K':
            break
         if cnt==14*2:
            res.append(len(data[i:j+1]))
         if cnt>28:
            break
print(max(res))
