from turtle import *
k=10
left(90)
pendown()
screensize(2000,2000)
tracer(0)
for _ in range(5):
    forward(37*k)
    right(90)
    forward(44*k)
    right(90)
penup()
backward(18*k)
right(90)
forward(29*k)
left(90)
pendown()
for __ in range(5):
    forward(31*k)
    right(90)
    forward(35*k)
    right(90)
penup()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*k,y*k)
        dot()
done()