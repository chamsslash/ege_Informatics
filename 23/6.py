def task23(start,end,k):
    if start>end:return 0
    if start==end and  ('***' not in k )and ("+++" not in k) :return 1
    return task23(start*2,end,k+"*")+task23(start+1,end,k+"+")
print(task23(1,20,''))