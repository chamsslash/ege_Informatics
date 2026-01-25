def g(s,h,end):
    if s >= 101:
        return h in end
    if h>=max(end):
        return False
    moves=[g(s+2,h+1,end),g(s*3,h+1,end)]
    if (((h+1)%2)==((end[0])%2)):
        return any(moves)
    else:
        return all(moves)
for x in range(1,101):
    if g(x,0,[2,4]) and not g(x,0,[2]):
        print(x)