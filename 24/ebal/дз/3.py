f=open("дз/Задание 2.txt")
a=[i.strip() for i in f]
res = 0
for s in a:
    for symb in s:
        if symb not in "0123456789+*":
            break
    else:
        res = max(res, eval(s))
print(res)