f = open("24_2.txt")
data = f.readline()
buff = data[0]
res = []
for i in range(len(data) - 1):
    if (
        data[i].isdigit()
        and data[i + 1].isdigit()
        and int(data[i]) + int(data[i + 1]) >= 10
    ):
        buff += data[i + 1]
    else:
        buff = data[i + 1]
    res.append(buff)
print(len(max(res, key=len)))
