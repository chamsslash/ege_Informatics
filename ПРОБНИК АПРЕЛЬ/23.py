def game(s,end):
    if s>end:
        return 0
    if s==end:
        return 1
    s=str(s)
    if int(s)<100 and s[-1]>s[0]:
        o1=int(f'{s[-1]}{s[0]}')
        return game(int(s) + 1, end)+game(o1,end)
    if int(s)>=100 and s[-1]>s[1]:
        o1=int(f'{s[0]}{s[-1]}{s[1]}')
        return game(int(s) + 1, end)+game(o1,end)

    return game((int(s)+1),end)
print(game(101,147))