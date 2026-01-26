from re import findall

with open("Задание 2.txt") as f:
    for x in f:
        op = findall(r'[+-/*]+', x)
        op1 = findall(r'\d+', x)
        print(len(max(max(op, key=len), max(op1, key=len), key=len)))
