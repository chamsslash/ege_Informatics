f = open("task3.txt")
a = f.readline()
buff = ""
res = 0
for i in range(len(a)):
    digit = a[i]
    if digit in "789":
        buff += digit
    # чтобы не было двойных знаков и нули были только в составе числа
    elif digit in "0*-" and len(buff) > 0 and buff[-1] not in "*-":
        buff += digit
    else:
        buff = ""
    if len(buff) >= 1 and buff[-1] not in "*-":
        res = max(res, eval(buff))
print(res)