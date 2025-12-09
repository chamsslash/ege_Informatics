f= open('26.1.txt')
kolvo = int(f.readline())
alls=[ int(x) for x in f]
alls120=[y for y in alls if y > 120]
alls120.sort()
sale = sum(alls120[:449])*0.25
res=sum(alls)-sale
res1 = max(alls120[:449])
print(res,res1)