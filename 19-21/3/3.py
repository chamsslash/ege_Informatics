from turtle import Pen


def game(s,h,end):
    if s>=81:
        return h in end
    if h >= max(end):
        return False
    mvs=[game(s+2,h+1,end),game(s*4,h+1,end)]
    if (h+1)%2==(end[0]%2):
        return any(mvs)
    else:
        return all(mvs)
for x in range(1,81):
    if game(x,0,[2,4]) and not game(x,0,[2]):
        print(x)