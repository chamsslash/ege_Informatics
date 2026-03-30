def f(r,h,end):
    if r>=364:
        return h in end
    if h>=max(end):return 0
    skls=[f(r+1,h+1,end),f(r+3,h+1,end),f(r*4,h+1,end)]
    return any(skls) if (h+1)%2==(end[0]%2) else all(skls)
print([i for i in range(1,364) if f(i,0,[2])])
print([i for i in range(1,364) if f(i,0,[3])])
print([i for i in range(1,364) if (f(i,0,[2,4]) and not f(i,0,[2]))])