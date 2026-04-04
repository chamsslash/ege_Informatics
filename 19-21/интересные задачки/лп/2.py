# print([bin(i)[2:] for i  in [3,5,9,17,33,65]])
# +2 единички в любом случае
def f(s,h,end):
    if s>=60:return h in end
    if h >=max(end):return False
    skills=[f(s+2,h+1,end),f(s*2,h+1,end)]
    if (h+1)%2==end[0]%2:
        return any(skills)
    else:return all(skills)
# print([i for i  in range(1,59) if f(i,0,[2])]) 15
print([i for i  in range(1,59) if f(i,0,[3])])
print(max([i for i  in range(1,59) if (f(i,0,[2,4]) and not f(i,0,[2]))]))