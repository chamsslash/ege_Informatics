for A in range(1,10_00):
    for x in range(1,10_00):
        if (((x&14!=0) or (x&17!=0)) <= ((x&18==0) <= (x&A!=0)))==False:
            break
    else:
        print(A)
