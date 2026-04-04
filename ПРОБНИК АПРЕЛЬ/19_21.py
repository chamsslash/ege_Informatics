def g(r1,r2,h,end):
    if r1*r2>=144:return h in end
    if h>=max(end):return False
    skills=[g(r1+1,r2,h+1,end),g(r1,r2+1,h+1,end),g(r1*2,r2,h+1,end),g(r1,r2*2,h+1,end)]
    if (h+1)%2==end[0]%2:
        return any(skills)
    else:
        return all(skills)
    # return any(skills)
# print([i for i in range(1,141) if g(3,i,0,[2])])
# 12
print([i for i in range(1,141) if g(3,i,0,[3])])
print([i for i in range(1,141) if (g(3,i,0,[2,4]) and not g(3,i,0,[2])) ])


