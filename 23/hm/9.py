def task23(start,end):
    if start==end:return 1
    if start>end:return task23(start-1,end)+task23(start//2,end)
    if start<end:return 0
print(task23(43,10)*task23(10,1))