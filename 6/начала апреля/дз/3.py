from turtle import *
k=20
tracer(0)
screensize(4000,4000)
left(90)
pendown()
for _ in range(2):
    forward(24*k)
    right(90)
    forward(20*k)
    right(90)
penup()
forward(7*k)
right(90)
forward(7*k)
left(90)
pendown()
for i in range(2):
    forward(60*k)
    right(90)
    forward(100*k)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*k,y*k)
        dot()
done()

