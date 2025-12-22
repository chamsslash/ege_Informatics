d = [w / 10 for w in range(28 * 10, 69 * 10 + 1)]
c = [w / 10 for w in range(40 * 10, 91 * 10 + 1)]
a=[]
for x in range(1,10_00):
    x= x/10
    if ((x in d) <= ((not(x in c) and not(x in a)) <= (not(x in d))))==0:
        a.append(x)
print(a)