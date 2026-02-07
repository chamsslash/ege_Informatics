for i in range(100,1000):
    i=str(i)
    summa=''
    a=str(int(i[0])+int(i[1]))
    b=str(int(i[1])+int(i[2]))
    if int(a)>int(b):
        summa= a+b
    if int(a)<int(b):
        summa=b+a
    if summa=='1815':
        print(i)
        break