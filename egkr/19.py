def f(r1,r2,h,end):
    if r1+r2>=65:
        return h in end
    if h>=max(end):
        return False
    skills=[f(r1+1,r2,h+1,end),f(r1,r2+1,h+1,end),f(r1*3,r2,h+1,end),f(r1,r2*3,h+1,end)]
    return  any(skills) if ((h+1)%2)==(end[0]%2) else all(skills)
# print(min([i for i in range(1,59) if f(6,i,0,[2])]))
print(([i for i in range(1,59) if f(6,i,0,[3])]))
print(([i for i in range(1,59) if (f(6,i,0,[2,4]) and not f(6,i,0,[2]))]))
# [10, 19]
# [18]