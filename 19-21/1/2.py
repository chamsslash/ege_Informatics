

def game(s,hod,end):
    if  (s)>=56:  return hod in end
    if s<56 : return  hod != max(end)
    moves=[game(s+1,hod+1,end),game(s*3,hod+1,end)]
    if (hod+1)%2==end[0]%2:
        return any(moves)
    else:
        return all(moves)
for x in range(1,56):
    if game(x,0,[2,4]) and  not game(x,0,[2]):
        print(x)