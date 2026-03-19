import math
for i in range(100,1000):

    o1=math.prod(int(digit) for digit in str(i) )
    o2=sum(int(digit) for digit in str(i) )
    res=str(max(o1,o2))+str(min(o1,o2))
    if res=='33621':
        print( i)