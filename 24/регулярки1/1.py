from re import findall

with open("Задание 1.txt") as f:
    a = f.read()

op = findall(r'[a-z]+', a)
print(len(max(op, key=len)) if op else 0)
