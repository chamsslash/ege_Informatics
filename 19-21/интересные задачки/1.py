import math

def f(s,h,end):
    if s==0:
        return h in end
    if h>=max(end):
        return False
    skills=[f((math.floor(s//3)),h+1,end)]
    if (s>=5):
        skills.append(f((s-5),h+1,end))
    if ((h+1)%2)==(end[0]%2):
        return any(skills)
    else:
        return all(skills)
print([i for i in range(1,10_00)if f(i,0,[2])])
print([i for i in range(1,10_00)if f(i,0,[3])])
print([i for i in range(1,10_00)if (f(i,0,[2,4]) and not f(i,0,[2]))])


