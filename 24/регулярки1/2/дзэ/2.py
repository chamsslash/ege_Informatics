with open('2/дзэ/Задание 2.txt') as f:
    from re import findall
    op = findall(r'\d+(?:[+\-*/]\d+)*', f.read().strip())
    print(len(max(op, key=len)))
