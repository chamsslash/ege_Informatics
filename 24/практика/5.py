with open("24.5.txt") as f:
    a = f.readline().strip()
    from re import findall
    op = findall(r"[789][0789]*(?:[*][789][0789]*)*",a)
    print(eval((max(op, key=eval))))
