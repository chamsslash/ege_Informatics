f=open('Задание 3.txt')
count_b,count_t=map(int,f.readline().split())
boxesi=[]
tapesi=[]
for _ in range(count_t):
    box,tape=map(int,f.readline().split())
    boxesi.append(box)
    tapesi.append(tape)
for _2 in range(count_b-count_t):
    box=int(f.readline())
    boxesi.append(box)
    tapesi.append(0)
gift=[]
boxesi.sort(reverse=True)
for boxi in boxesi:
    if len(gift)==0:
        if boxi in tapesi:
            gift.append(boxi)
    elif boxi in tapesi and gift[-1]-boxi>=9:
        gift.append(boxi)
print(len(gift),gift[0])

# Надо найти разницу между самой большой в теории возможно взятой коробкой и самой маленькой в теории влзможной взятой коробкой