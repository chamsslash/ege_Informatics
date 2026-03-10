f=open("17.14.txt")
data=[int(i)for i in f]
cnt=0
twos=[i for i in data if len(str(abs(i)))==2]
min2=min(twos)
sums=[]
max2=max(twos)
for i in range(len(data)-2):
    a=data[i]
    b=data[i+1]
    c=data[i+2]
    # тк могут быть и отрицительные чиселки
    if ((((len(str(abs(a)))==2)+(len(str(abs(b)))==2)+(len(str(abs(c)))==2))>=2) and ((a+b+c)>(max2+min2))):
        cnt+=1
        sums.append(a+b+c)

print(cnt,max(sums))
