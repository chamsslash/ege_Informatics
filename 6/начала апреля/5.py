from turtle import *
left(90)
speed(0)
k=3
screensize(3000,3000)
pendown()
right(180)
for _ in range(9):
    forward(59*k)
    left(90)
    forward(84*k)
    left(90)
penup()
forward(18*k)
left(90)
forward(38*k)
right(90)
pendown()
for _ in range(9):
    forward(120*k)
    right(90)
    forward(99*k)
    right(90)
penup()
tracer(0)

for x in range(-150,150):
    for y in range(-150,150):
        setpos(x*k,y*k)
        dot()
done()