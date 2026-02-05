import math

for a in range(0,10000):
    for x in range(0,10000):
        if ((((x&52)!=0)and (x&48==0))<=(not(x & a == 0)))==0:
            break
    else:
        print(a)
