def to31(x):
    summa = 0
    while x>0:
        if (x%31)<=17:
            summa+=x%31
        x=x//31
    return  summa
f=3*(289**2024)+81*(49**121)-9*(16**81)-6011
print(to31(f))