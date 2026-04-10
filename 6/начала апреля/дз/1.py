from  turtle import *
screensize(2000,2000)
tracer(0)
left(90)
k=20
pendown()
for _ in range(6):
    forward(10*k)
    right(270)
penup()
forward(3*k)
right(270)
forward(5*k)
right(90)
pendown()
for __ in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)
penup()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot(3)
print(11*11+11*13-48)
done()
