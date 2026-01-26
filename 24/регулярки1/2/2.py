with open('2/task2.txt') as f:
    from re import findall
    op = findall(r'(?:LDR)+(?:LD?)?', f.readline())
    print(len(max(op, key=len)))
