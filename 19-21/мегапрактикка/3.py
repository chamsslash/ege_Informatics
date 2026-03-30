def f(r,r2,h,end):
    if r*r2>=522:
        return h in end
    if h>=max(end):return 0
    skls=[f(r+4,r2,h+1,end),f(r,r2+4,h+1,end),f(r+7,r2,h+1,end),f(r,r2+7,h+1,end)]
    return any(skls) if (h+1)%2==(end[0]%2) else all(skls)
print([i for i in range(1,87) if f(6,i,0,[2])])
print([i for i in range(1,87) if f(6,i,0,[3])])
print([i for i in range(1,87) if (f(6,i,0,[2,4])and not f(6,i,0,[2]))])