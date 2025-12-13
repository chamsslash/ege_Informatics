a=list(range(3,68))
b=[i for i in range(2,127) if 127 % i == 0]
print(b)
for y in range(1,10000):
    c = [i for i in range(2, y) if y % i == 0]
    if c:
        for x in range(1,10_00):
            if ((x in c) <=((x in a)and(not(x in b))))==0:
                break
        else:
            print(y)
            break
