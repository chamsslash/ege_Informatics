with open('2/task1.txt') as f:
    from re import findall
    op = findall(r"9?8?7?6?5?4?3?2?1?", f.readline())
    print(len(max(op, key=len)))