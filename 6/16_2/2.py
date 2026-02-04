from turtle import *

pendown()
k = 100
speed(0)
begin_fill()

for i in range(3):
    forward(111*k)
    right(120)

end_fill()
canvas=getcanvas()

c=0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            c += 1

print(c)
done()