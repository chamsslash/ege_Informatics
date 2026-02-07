def task23(start,end):
    if start>end or start==23:return 0
    if start==end:return 1
    return task23(start+1,end)+task23(start*2,end)
print(task23(4,66)* task23(66,93))
    