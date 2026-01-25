def g(f,s,h,end):
    if (s+f)>=66:return h in end
    if h >=max(end):return False
    moves=[g(f+1,s,h+1,end),g(f,s+1,h+1,end),g(f*3,s,h+1,end),g(f,s*3,h+1,end)]
    if ((h+1)%2) == ((end[0])%2):
        return any(moves)
    else:
        return all(moves)
x=6
for y in range(1,60):
    if g(x,y,0,[2,4]) and not g(x,y,0,[2]):
        print(y)