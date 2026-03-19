f=open('task1.txt')
poss_res=[]
n,m,k=map(int,f.readline().split())
# хранит
av_best_ryads=[m]*(k+1)
for i in f:
    ryad,mesto=map(int,i.split())
    av_best_ryads[mesto]=min(av_best_ryads[mesto],ryad-1)
# итерация по местам(по индексам )
for n in range(1,len(av_best_ryads)-1):
    # ryads
    l_seat,r_seat=av_best_ryads[n],av_best_ryads[n+1]
    poss_res.append([min(l_seat,r_seat),n,n+1])
print(poss_res)
print(max(poss_res))

