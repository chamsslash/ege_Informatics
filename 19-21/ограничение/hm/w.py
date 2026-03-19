def f(r,h,end):
    if r<=22 and r>=16:
        return h in end
    elif r<=22 and r<=16:
        return (h%2)!=(end[0]%2)
    if h>=max(end):return 0
    skls=[f(r//2,h+1,end),f(r-1,h+1,end)]
    return  any(skls)    if ((h+1)%2)==(end[0]%2) else all(skls)
print([p for p in range(23,10_000) if f(p,0,[2])])
print([p for p in range(23,10_000) if f(p,0,[3])])
print([p for p in range(23,10_000) if (f(p,0,[2,4]) and not f(p,0,[2]))])

