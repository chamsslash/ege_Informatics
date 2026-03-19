def f(r,r1,h,end):
    if r+r1>=56:
        return h in end
    if h>=max(end):
        return 0
    skls=[]
    for dob in range(1,min(r,r1)+1):
        if r>r1:skls.append( f(r,r1+dob,h+1,end) )
        elif r<r1:skls.append( f(r+dob,r1,h+1,end) )
        else:
            skls.append( f(r,r1+dob,h+1,end) )
            skls.append( f(r+dob,r1,h+1,end))
    return any(skls) if ((h + 1) % 2) == (end[0] % 2) else all(skls)
print(min([(i+i1) for i in range(1,49)  for i1 in range(1,49)if f(i,i1,0,[1])]))
print([i1  for i1 in range(1,49)if f(7,i1,0,[3])])
print([i1  for i1 in range(1,49)if (f(7,i1,0,[2,4]) and not f(7,i1,0,[2]))])




