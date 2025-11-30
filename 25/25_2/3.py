for yaru in range(600_001,600_001+1000):
    M=0
    for delitel in range(2,yaru):
        if yaru % delitel == 0:
            M=delitel+(yaru//delitel)
            break
    if str(M)[-1]=='4':
        print(yaru,M)
