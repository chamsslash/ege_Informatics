from turtle import *
k=10
cnt=0
tracer(0)
pendown()
begin_fill()
for i in range(3):
    right(45)
    forward(k*12)
    right(45)
right(315)
forward(k*12)
for i in range(2):
    right(90)
    forward(k*12)
end_fill()
canva=getcanvas()
penup()
for x in range(-200,200):
    for y in range(-200,200):
        if (canva.find_overlapping(x*k, y*k,x*k, y*k))==(5,):
            cnt+=1
print(cnt)
done()