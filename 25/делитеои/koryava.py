for n in range(800_001, 800_001+1000):
    dels=[]
    for uwu in range(2,n):
        if n%uwu==0:
            dels.append(uwu)
    F=0
    if len(dels)>0:
        F=dels[0] * dels[-2]
        if F!=0 and F%sum(dels[:2])==0:
            print(n,F)