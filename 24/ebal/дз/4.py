f=open("дз/Задание 3.txt")
a=[i.strip() for i in f]
res = 0
flag=True
buff=''
for s in a:
    for symb in s:
        if symb not in "0123456789+*-":
            break
    else:
        for sym in s:
            if sym=="-":flag=False
            elif sym in'+*':
                flag=True
                buff+=sym
            elif flag :
                buff+=sym
        if buff[0] in '+*':
            buff=buff[1:]
        res=max(res, eval(buff))
        buff=''
        flag=True
print(res)