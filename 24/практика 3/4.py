f=open('24.4.txt')
res=[]
data=f.readline().strip()
indexes=[i for i in range(len(data)) if data[i]=='A']
for aindex in range(len(indexes)-34):
    o1=indexes[aindex+34]-indexes[aindex]+1
    res.append(o1)
print(min(res))