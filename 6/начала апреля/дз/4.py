from turtle import *
left(90)
screensize(2000,2000)
k=20
tracer(0)
for i in range(2):
    forward(10*k)
    left(270)
    backward(20*k)
    right(90)
penup()
forward(15*k)
right(90)
backward(7*k)
right(90)
pendown()
for ii in range(2):
    forward(13*k)
    right(90)
    forward(3*k)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot()
print(11*21+14*4-36)
done()