f=3*289**2024+81*49**121-9*16**81-6011
def to31(fx):
    summa=0
    while fx>0:
        if fx%31<=17:
            summa+=fx%31
        fx=fx//31
    return summa
print(to31(f))