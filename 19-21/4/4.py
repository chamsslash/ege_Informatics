from math import ceil

def g(f,s,h,end):
    if (s+f)<=22:return h in end
    if h >=max(end):return False
    moves=[g(f-1,s,h+1,end),g(f,s-1,h+1,end),g(ceil(f/2),s,h+1,end),g(f,(ceil(s/2)),h+1,end)]
    if ((h+1)%2) == ((end[0])%2):
        return any(moves)
    else:
        return all(moves)
x=10 
for y in range(12,1000):
    if g(x,y,0,[2,4]) and not g(x,y,0,[2]):
        print(y)
