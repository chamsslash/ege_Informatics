f = open("24_1.txt")
data = f.readline()
prs = data[0]
res = []
for i in range(len(data) - 1):
    if data[i].isdigit() and data[i + 1].isdigit():
        prs += data[i + 1]
    else:
        prs = data[i + 1]
    if prs.isdigit() and int(prs) % 2 != 0:
        res.append(int(prs))
print(max(res))
