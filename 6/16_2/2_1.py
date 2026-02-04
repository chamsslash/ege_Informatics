from turtle import *
tracer(0)
k=30
pendown()
screensize(2000,2000)
for _ in range(4):
    forward(12*k)
    right(90)
    forward(16*k)
    right(90)
penup()
forward(6*k)
right(90)
forward(8*k)
left(90)
pendown()
for _ in range(4):
    forward(11*k)
    right(90)
    forward(8*k)
    right(90)
    
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot()
        
done()