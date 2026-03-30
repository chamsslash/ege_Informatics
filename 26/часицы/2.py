f=open('Задание 2.txt')
cnt=int(f.readline())
res=[]
ryadi_poziciy=[[] for __ in range(cnt+1)]
for step in f:
    ryad,pos =map(int,step.split())
    ryadi_poziciy[ryad].append(pos)
for ryad in ryadi_poziciy:
    ryad.append(-1000000)
    ryad.append(1000000)
    ryad.sort()
    print(ryad)
    isolat=0
    for index_of_dot in range(1,len(ryad)-1):
        up=ryad[index_of_dot-1]
        mid=ryad[index_of_dot]
        down=ryad[index_of_dot+1]
        if (abs(up-mid)>1000 and abs(mid-down))>1000:
            isolat+=1
    res.append([isolat,-(ryadi_poziciy.index(ryad))])
res.sort(reverse=True)
print(res[:10])
print(max(res))

# =ЕСЛИМН(   И(A1<>A2;A2=A3); ЕСЛИ(ABS(B2-B3)>1000;1;0);
# И(A1=A2;A2=A3); ЕСЛИ(И(ABS(B2-B3)>1000;ABS(B2-B1)>1000);C1+1;1);
# И(A1=A2;A2<>A3); ЕСЛИ(ABS(B1-B2)>1000;C1+1;1)
# ;И(A1<>A2;A2<>A3);1)