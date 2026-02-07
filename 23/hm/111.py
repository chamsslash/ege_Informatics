def task23(start,end):
    if start>end or start==35:return 0
    if start==end:return 1
    return task23(start*3,end)+task23(start*4,end)+task23(start+1,end)
print(task23(3,10)*task23(10,70))