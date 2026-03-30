def game(rock,h,end):
    if 81<=rock<=145:
        return h in end
    if h >= max(end) :
        return 0
    skills=[game(rock*2,h+1,end),game(rock+2,h+1,end)]
    return  any(skills) if ((h+1)%2==end[0]%2) else all(skills)
print([i for i in range(1,80) if game(i,0,[2])])
print([i for i in range(1,81) if (game(i,0,[3]) and not game(i,0,[1]))])
print([i for i in range(1,81) if (game(i,0,[2,4]) and not game(i,0,[2]))])