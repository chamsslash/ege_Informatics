from turtle import *
left(90)
screensize(2000,2000)
pendown()
k=20
tracer(0)
right(315)
for __ in range(7):
    forward(k*12)
    right(45)
    forward(k*6)
    right(135)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot()
done()
# 40