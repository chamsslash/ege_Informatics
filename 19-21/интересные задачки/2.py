def f(s,h,end):
    if s>=72:return h in end
    if h>=max(end):return False
    skls=[f(s+3,h+1,end),f(s*2,h+1,end)]
    if ((h+1)%2)==(end[0]%2):
        return any(skls)
    else:return all(skls)
# print([i for i in range(1,70) if f(i,0,[2])])
# 18
print([i for i in range(1,70) if f(i,0,[3])])
print([i for i in range(1,70) if (f(i,0,[2,4]) and not f(i,0,[2]) )])

# у всех 3 единицы поэтому просто при любом n у нас изменние единичек ранво 3
# print([bin(i)[2:] for i in [7,19,131]])