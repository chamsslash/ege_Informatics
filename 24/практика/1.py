f = open("24.1.txt")
a = f.readline()
a = "NT" + a + "NT"
a = a.replace("NT", "Z")
z_indexes = [i for i, char in enumerate(a) if char == "Z"]
res = []
for i in range(len(z_indexes) - 192):
    res.append(z_indexes[i + 192] - z_indexes[i] +194-1 )

print(max(res))
