for a in range(1,10000):
    for x in range(1,1000):
        for y in range(1,1000):
            if (((y+42<a)and(17-x<a)) or ((y+3)*x>71))==0:
                break
        if (((y + 42 < a) and (17 - x < a)) or ((y + 3) * x > 71)) == 0:
            break
    else:
        print(a)