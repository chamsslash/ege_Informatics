for x in range(2):
    for y in range(2):
        for z in range(2):
            # if ((y or z) == ((z and (not(y))) <= (not(x)))) == 0:
            if ((z<=(not(x)) and y)<=(z==y))==0:
                print(x,y,z)