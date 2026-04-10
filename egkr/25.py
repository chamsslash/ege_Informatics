import math

for n in range(700_001,700_001+1000):
    for d in range(17,n,10):
        # проверка на делител
        if n%d==0:
            print(n,d)
            break
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167