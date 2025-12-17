def gay(rocks,stage,end):
    if rocks<=30:return stage in end
    if stage>=max(end):return False
    moves=[gay(rocks-5,stage+1,end),gay(rocks-3,stage+1,end),gay(rocks//4,stage+1,end)]
    if ((stage+1)%2==end[0]%2):return any(moves)
    else:return all(moves)
# 1-3-5-7 петя
# 2-4-6-8  выаня
print([r for r in range(31,1000) if gay(r,0,[2])])
print([r for r in range(31,1000) if gay(r,0,[2,4])])