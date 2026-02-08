f=open('Задание 1.txt')
cnt=f.readline()
alls=([int(item) for item in f])
alls.sort(reverse=True)
sale=alls[:int(cnt)//3]
first=sum(alls)-sum(sale)
sale2=0
for index,item in enumerate(alls):
    if ((index+1)%3)==0:
        sale2+=item
second=sum(alls)-sale2
print(first,second)
