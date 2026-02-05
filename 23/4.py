def task23(start, end,d):
    if start > end or start==50:return 0
    if start==end:return 1
    return task23(start+d,end,d)+task23(start*4,end,d)
sum=0
for d in range(1,1001):
    sum += task23(1,10,d)* task23(10,100,d)
print(sum)
