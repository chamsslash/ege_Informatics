f = open("Задание 1.txt")
ib=[int(x) for x in f]
good=[int(a) for a in ib if int(a)>120]
good.sort()
skidka=sum((good[:len(good)//2]))*0.25
full=sum(ib)-skidka
print(full,max(good[:len(good)//2]))
# 447166.25 522