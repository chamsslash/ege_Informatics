def task23(start, end,k):
    if start > end :return 0
    if start == end and k ==1 :return 1
    return task23(start*2,end,k+1)+task23(start*3,end,k+1)+task23(start+1,end,k)+task23(start+2,end,k)
print(task23(1,16,1))