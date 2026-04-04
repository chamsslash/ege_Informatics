from turtle import *
k=7
left(90)
screensize(2000,2000)

pendown()
for _ in range(3):
    forward(k*27)
    right(90)
    forward(k*12)
    right(90)
penup()
forward(4*k)
right(90)
forward(6*k)
left(90)
pendown()
for __ in range(4):
    forward(83*k)
    right(90)
    forward(77*k)
    right(90)
penup()
tracer(0)
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*k,y*k)
        dot()
done()