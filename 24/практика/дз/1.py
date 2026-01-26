with open("дз/Задание 1.txt") as f:
    a = f.readline().strip()
    a = "RO" + a + "RO"
    a = a.replace("RO", "Z")
    res = []
    z_list = [i for i, a in enumerate(a) if a == "Z"]
    for i in range(len(z_list) - 359):
        res.append(z_list[i + 359] - z_list[i] + 360-1)

    print(max(res))