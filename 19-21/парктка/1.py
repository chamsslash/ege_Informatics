def g(r,h,end):
    if r<=19 :return h in end
    if  h >= max(end):return False

    skills=[g(r-1,h+1,end)]
    if r%3==0:
        skills.append(g(r//3,h+1,end))
    else:
        skills.append(g(r-2,h+1,end))
    if r%5==0:
        skills.append(g(r//5,h+1,end))
    else:
        skills.append(g(r-3,h+1,end))
    # будет ходить наш люьимчмк
    if ((h+1)%2)==(end[0]%2) :
        return any(skills)
    else:
        return all(skills)
for i in range(20,200):
    if g(i,0,[2]):
        print('20:' ,i)
    if g(i,0,[3]):
        print('21:',i)
    if g(i, 0, [2,4]) and not g(i,0,[2]):
        print('22:',i)


