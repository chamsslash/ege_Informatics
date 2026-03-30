a=list(range(7,26+1))
b=[i for i in range(2,77) if 77%i==0]
for y in range(1,10_000):
    c=[i for i in range(2,y) if y%i==0]
    if c :
        for x in range(1,10_000):
            if ((x in c) <= ((x in a) and (not(x in b)))) ==0 :
                break
        else:
            print(y)
            break