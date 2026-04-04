from turtle import *
left(90)
screensize(2000,2000)
# tracer(0)
pendown()
k=15
for i in range(3):
    pendown()
    for ii in range(2):
        forward(10*k)
        right(90)
        forward(10*k)
        right(90)
    penup()
    forward(10*k)
    right(90)
    forward(5*k)
    right(90)
# for x in range(-20,20):
#     for y in range(-20,20):
#         setpos(x*k,y*k)
#         dot()
done()