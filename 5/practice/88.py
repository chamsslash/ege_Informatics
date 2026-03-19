for n in range(100,1000):
    digits=[int(i)for i in str(n)]
    o1=(digits[0]**2)+(digits[1]**2)
    o2=(digits[1]**2)+(digits[2]**2)
    r=str(max(o1,o2))+str(min(o1,o2))
    if r=='9752':
        print(n)