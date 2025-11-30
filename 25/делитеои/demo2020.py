for n in range(123_456,123_487+1):
    dels=[]
    for d in range(1,n+1):
        if n%d == 0:
            dels.append(d)
    if len(dels)==6:
        print(dels,'---',n)