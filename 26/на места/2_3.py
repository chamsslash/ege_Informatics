f=open('task2.txt')
zan_c,r_c,m_c=map(int,f.readline().split())
zanatye_scheme=[[] for o in range(m_c+1)]
res=[]
for zana in f:
    r,m=map(int,zana.split())
    zanatye_scheme[m].append(r)
for ryad_mesta in zanatye_scheme[2:]:
    ryad_mesta.append(0)
    ryad_mesta.append((r_c+1))
    ryad_mesta.sort(reverse=True)
    for place in range(len(ryad_mesta)-1):
        pl1=ryad_mesta[place]
        pl2=ryad_mesta[place+1]
        kolvo_free=pl1-pl2-1-1
        res.append([kolvo_free,pl1-1])
res.sort(reverse=True)
print(res)
print(max(res))
