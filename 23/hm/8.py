def task23(start,end,num):
    if start == end and "".join(sorted(num)) == num:
        return 1
    if start > end:
        return 0
    return (
        task23(start*3,end,num+'1')
        + task23(start*2,end,num+'2')
        + task23(start+2,end,num+'3')
        + task23(start+1,end,num+'4')
    )

print(task23(2,25,""))
