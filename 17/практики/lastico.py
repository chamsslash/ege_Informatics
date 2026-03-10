f=open('17.16.txt')
data=[int(i)for i in f]
sums=[]
cnt=0
lasts250=[i for i in data if (str(abs(i)))[-3:]=='250']
l=min(lasts250)
for i in range(len(data)-2):
    a=data[i]
    b=data[i+1]
    c=data[i+2]
    if (a%2==0 and b%2==0 and c%2==0) and sum(data[i:i+3])>l:
        cnt+=1
        sums.append(a+b+c)
print(cnt,max(sums))
