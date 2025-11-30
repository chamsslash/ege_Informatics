for z in range(100_356,100_367+1):
    dels=[]
    for d in range(1,z+1):
        if z%d == 0:
            dels.append(d)
    if len(dels)==4:
        print(z,"---",dels)