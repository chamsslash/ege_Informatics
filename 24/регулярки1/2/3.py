res=[]
with open('2/task3.txt') as f:
    from re import findall
    for x in f:
        op = findall(r'\d+(?:[+\-*/]\d+)*',x)
        #findall(r'\d+(?:[+\-*/]\d+)*',
        if op:
            res.append(max(op, key=len))
print(max(res, key=len))
print(len(max(res, key=len)))
    