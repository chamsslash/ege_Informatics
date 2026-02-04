from turtle import *
k=550
cnt=0
speed(0)
begin_fill()
for _ in range(6):
    right(90)
    forward(120*k)
    right(90)

    forward(14*k)
end_fill()
canvas=getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
            cnt += 1
print(cnt)
done()