f = open("26.2.txt")
a=int(f.readline())
alls=[int(x) for x in f]
alls.sort()
neg_alls=alls[-len(alls)//4:]
sale_u=sum(neg_alls)*0.5
sale_l=sum(alls[:len(alls)//4])*0.5
print(sum(alls)-sale_u,sum(alls)-sale_l)