
from re import findall
cnt=0
with open("Задание 3.txt") as f:
    for i in f:
        num=i.strip()
        op = findall(fr'\+[78]{1}\-\([0-9]{3}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}', num)
        if op:cnt+=1


print(cnt)
