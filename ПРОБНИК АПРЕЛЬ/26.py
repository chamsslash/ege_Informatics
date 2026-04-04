f=open('26.txt')
k_yacheek=int(f.readline())
cnt=0

k_pass=int(f.readline())
data=[list(map(int,i.split()))for i in f]
data.sort()
yacheq=[[0] for i in range(k_yacheek)]
# for start,end in data:
last_used=0
for start,stop in (data):
    num=0
    for ya in yacheq:
        num+=1
        yash_osvoboditsa = ya[0]
        if start>yash_osvoboditsa:
            ya[0]=stop
            # перезаписываем именно таймер в списке с ячейками
            last_used=num
            cnt+=1
            break
        else:
            continue
print(cnt,last_used)
