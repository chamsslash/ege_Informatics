f=open('Задание 5.txt')
kolvo=int(f.readline())
data=[list(map(int,i.split()) )for i in f]
last_ested=0
begin=[]
end=[]
for num,i in enumerate(data,1):
    if i[0]<i[1]:
        begin.append([i[0],num])
        del i
        last_ested=num
    else:
        end.append([i[1],num])
        del i
        last_ested=num
print(max(end)[-1],len(begin))
