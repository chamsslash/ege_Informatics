res = []
f = open("task3.txt")
a = [i.strip() for i in f]
for i, z in enumerate(a):
    eva = 0
    try:
        eva = eval(z)
    except:
        print("Ошибка в строке:", i + 1, z)
        pass
    for dig in z:
        if dig in "+-/*":
            pass
        else:
            if dig not in "0123456789":
                break
    else:
        # по условию нумерация с 1
        res.append([eva, i + 1])

print(max(res))
