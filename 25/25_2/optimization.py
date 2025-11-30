for zov in range(23456,123_456):
    dels=[]
    #Оптимизация с помощью корня ня
    if zov**(1/2)%1==0:
        for d in range(2,zov) :
            if zov % d == 0 :
                dels.append(d)
        if len(dels)==3:
            print(zov,"---",dels)