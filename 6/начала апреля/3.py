from turtle import *
k=15
pendown()
screensize(2000,2000)
tracer(0)
for _ in range(9):
    forward(27*k)
    right(90)
    forward(30*k)
    right(90)
penup()
forward(3*k)
right(90)
forward(6*k)
left(90)
pendown()
for __ in range(9):
    forward(77*k)
    right(90)
    forward(66*k)
    right(90)

penup()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*k,y*k)
        dot()
done()