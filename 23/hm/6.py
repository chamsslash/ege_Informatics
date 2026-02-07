def task23(start,end):
    if start>end or start == 5:return 0
    if start==end:return 1

    return task23(start+1,end)+task23(start*3,end)
print(task23(1,21))