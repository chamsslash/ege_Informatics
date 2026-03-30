f=open('26_1.txt')
zan_c,ryad_c,mest_c=map(int,f.readline().split())
av=[]
pole=[ryad_c]*(mest_c+1)
for x in f:
    ryad,mest=map(int,x.split())
    pole[mest]=min(pole[mest],ryad-1)

for number in range(1,len(pole)-1):
    min_mun=min(pole[number],pole[number+1])
    av.append([min_mun,-number,-(number+1)])
av.sort(reverse=True)
print(max(av))