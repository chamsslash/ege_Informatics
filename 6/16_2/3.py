k=100
cnt=0
from turtle import *
speed(0)
begin_fill()
for _ in range(3):
    forward(123*k)
    right(120)
end_fill()
canvas=getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            cnt += 1
print(cnt)
done()