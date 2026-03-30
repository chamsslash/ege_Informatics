def f(rocks,hod,end):
    if 13<=rocks<=16:
        return hod in end
    if hod>=max(end):
        return 0
    skls=[f(rocks//2,hod+1,end),f(rocks-1,hod+1,end)]
    return any(skls) if (hod+1)%2==(end[0]%2) else all(skls)
print([rocki for rocki in range(17,10_000) if f(rocki,0,[2])])
print([rocki for rocki in range(17,10_000) if f(rocki,0,[3])])
print([rocki for rocki in range(17,10_000) if (f(rocki,0,[2,4]) and not f(rocki,0,[2]))])