from turtle import *
cnt=0
k=200
speed(0)
begin_fill()
right(90)
for _ in range(3):
    right(45)
    forward(k*12)
    right(45)
right(315)
forward(k*12)
for __ in range(2):
    right(90)
    forward(k*12)
end_fill()
canvas=getcanvas()
for x in range(-100,100):
    for y in range(-100,100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            cnt += 1
print(cnt)
done()