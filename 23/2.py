def task23(start,end):
    if start==end:return 1
    if start>end:return task23(start-2,end)+task23(start//2,end)+task23(start//3,end)
    if start<end:return 0
print(task23(45,31)*task23(31,10))