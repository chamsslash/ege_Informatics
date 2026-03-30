def f(r,h,end):
    if 65<=r<=100:
        return   h in end
    elif 65<=r and r>=100:
        return (h%2)!=(end[0]%2)
    if h>=max(end) :return 0
    skls=[f(r+1,h+1,end),f(r*3,h+1,end)]
    return any(skls) if (h+1)%2==(end[0]%2) else all(skls)
# print([i for i in range(1,65) if f(i,0,[2])])
# print([i for i in range(1,65) if (f(i,0,[3]))])
print([i for i in range(1,65) if( f(i,0,[2,4]) and not f(i,0,[2])) ])


