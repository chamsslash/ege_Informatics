from re import fullmatch


cnt=0
with open('2/дзэ/Задание 3.txt') as f:
    from re import findall
    for x in f:
        # не забыть strip(),чтобы отбросить /n
        op = fullmatch(r'\d+(?:[+\-*/]\d+)*',x.strip())
        if op:
            cnt+=1
print(cnt)