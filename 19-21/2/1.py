def game(f,s,hod,end):
    if (f+s)>=89:return hod in end
    if (f+s)<89 and hod ==max(end):
        return False
    if ((hod+1)%2)==(end[0]%2):
        return game(f+2,s,hod+1,end) or game(f*3,s,hod+1,end) or game(f,s*3,hod+1,end)or game(f,s+2,hod+1,end)
    else:
        return game(f+2,s,hod+1,end) and game(f*3,s,hod+1,end) and game(f,s*3,hod+1,end)and  game(f,s+2,hod+1,end)
stone1=10
for stone2 in range(1,89):
    if game(stone1,stone2,0,[2,4]) and not game(stone1,stone2,0,[2]):
        print(stone2)