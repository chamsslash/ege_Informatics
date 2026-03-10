def prt(a,b,c):
    return (a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2)
cnt=0
for A in range(0,100,2):
    if A != 0:
        for x in range(1,10_00):
            for y in range(1,10_00):
                if ( prt(16,y,A) or prt(x,y,A) == (x+A<85))==0:
                    break
            if (prt(16, y, A) or prt(x, y, A) == (x + A < 85)) == 0:
                break
        else:
            print(A)
            cnt+=1

print(cnt)