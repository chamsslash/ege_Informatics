def f(r,h,end):
    if r<=10:
        return h in end
    if h>=max(end):
        return False
    skls = [f(r - 3, h + 1, end), f(r - 6, h + 1, end)]

    if (h+1)%2==0:
        skls=[f(r-5,h+1,end),f(r-8,h+1,end)]

    return any(skls) if (h+1)%2==(end[0]%2) else all(skls)
print([i for i in range(11,43) if f(i,0,[2])])
print([i for i in range(11,43) if (f(i,0,[3]) and not f(i,0,[1]))])
print([i for i in range(11,43) if (f(i,0,[2,4]) and not f(i,0,[2]))])

