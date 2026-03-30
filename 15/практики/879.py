for A in range(1,10000):
    for x in range(1,10_00):
        for y in range(1,10_00):
            if ((y-2*x < A) or (x>=25)  or (y>=40))==0:
                 break
        if ((y - 2 * x < A) or (x >= 25) or (y >= 40)) == 0:
            break
    else:
        print(A)
        break