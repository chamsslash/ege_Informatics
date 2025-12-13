d= list(range(30,45+1))
def Del(n,m):
    return n % m==0
for a in range(1,1000):
    for x in range(1,1000):
        if(((not Del(x, 7)) and (x not in {52, 60, 68}))<=(
                    ((abs(x - 25) <= 10) <= (x in d))
                    or ((x & a) != 0))) == False:
            break
    else:
        print(a)
