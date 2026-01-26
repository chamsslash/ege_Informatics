from re import findall

with open('2/дзэ/Задание 1.txt') as f:
    op = findall(r'(?:XYZ)+(?:XY?)?', f.read().strip())
    print(len(max(op, key=len)))