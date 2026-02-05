def task23(start,end):
    if start>end:return 0
    if start==end:return 1
    return task23(start+1,end)+ task23(int(bin(start)[2:]+bin(start%7)[2:]),end)
print(task23(1,int("101010101",2)))

def task23(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return task23(start + 1, end) + task23(int(bin(start)[2:] + bin(start % 7)[2:], 2), end)

print(task23(1, int("101010101", 2)))
