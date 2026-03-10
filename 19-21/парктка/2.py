def g(r,h,end):
    if r<=19: return h in end
    if h>=max(end):
        return False
    skills=[g(r-5,h+1,end)]
    if r%2==0:
        skills.append(g(r//2,h+1,end))
    if r %3==0:
        skills.append(g(r//3,h+1,end))
    if ((r%2)!=0 and (r%3)!=0):
        skills.append(g(r+1,h+1,end))
    if (h + 1)%2==(end[0] % 2):return any(skills)
    else:return all(skills)
print([ i for i in range(20,200) if g(i,0,[2])])
print([ i for i in range(20,200) if g(i,0,[3]) and not g(i,0,[1])])
print([ i for i in range(20,200) if g(i,0,[2,4]) and  not g(i,0,[2])])