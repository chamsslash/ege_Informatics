def f(r,r1,h,end):
    if (r*r1)>=184:
        return h in end
    if h>=max(end):return 0
    skls=[f(r+1,r1,h+1,end),f(r,r1+1,h+1,end),f(r*2,r1,h+1,end),f(r,r1*2,h+1,end)]
    return any(skls) if (h+1)%2==end[0]%2 else all(skls)
print([i for i in range(1,182) if f(2,i,0,[2])])
print([i for i in range(1,182) if (f(2,i,0,[3]) and not f(2,i,0,[1]))])
print([i for i in range(1,182) if (f(2,i,0,[2,4]) and not f(2,i,0,[2]))])
