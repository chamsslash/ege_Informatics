def task23(s,e):
    if s >e or s == 15:
        return 0
    if s == e: return 1
    return  task23(s+1,e)+task23(s*2,e)+task23(s**2,e)
print(task23(3,30))