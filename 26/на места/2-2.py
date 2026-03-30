f=open('task2.txt')
zan,ryad_c,mest_c=map(int,f.readline().split())
zan_mesta=[[] for i in range(mest_c+1)]
res=[]
for z in f:
    ryad,mesto=map(int,z.split())
    zan_mesta[mesto].append(ryad)
for zan_na_mesto in zan_mesta[2:]:
    zan_na_mesto.append(0)
    zan_na_mesto.append(ryad_c+1)
    zan_na_mesto.sort(reverse=True)
    for zanyat_num in range(len(zan_na_mesto)-1):
        kolvo_svob=zan_na_mesto[zanyat_num]-zan_na_mesto[zanyat_num+1]-1-1
        res.append([kolvo_svob,zan_na_mesto[zanyat_num]-1])
res.sort(reverse=True)
print(res)
print(max(res))