def g(s,f,h,end):
    if (s+f)>=105:
        return h in end
    if h>=max(end):
        return False
    moves=[g(s+4,f,h+1,end),g(s*3,f,h+1,end),g(s,f+4,h+1,end),g(s,f*3,h+1,end)]

    if ((h+1)%2)==(end[0]%2):
        return any(moves)
    else:
        return all(moves)
x=4
for y in range(1,101):
    if g(x,y,0,[2,4]) and not g(x,y,0,[2]):
        print(y)