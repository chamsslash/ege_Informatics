from  turtle import *
tracer(0)
left(90)
k=20
screensize(2000,2000)
pendown()
for ___ in range(6):
    forward(14*k)
    right(90)
    forward(28*k)
    right(90)
penup()
forward(3*k)
right(90)
forward(7*k)
left(90)
pendown()
for iio in range(7):
    forward(58*k)
    right(90)
    forward(80*k)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*k,y*k)
        dot()
done()

