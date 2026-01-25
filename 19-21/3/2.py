def g(s,h,end):
    if s>=101:
        return h in end
    if h == max(end):
        return False
    mvs=[g(s+4,h+1,end),g(s*5,h+1,end)]
    if (h+1)%2==(end[0]%2):
        return any(mvs)
    else:
        return all(mvs)
for i in range(1,100):
    if g(i,0,[2,4]) and not g(i,0,[2]):
        print(i)