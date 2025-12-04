from turtle import *
left(90)
tracer(0)
pendown()
k=300
begin_fill()
for i in range(111):
    forward(123*k)
    right(120)
end_fill()
penup()
cnt=0
canva=getcanvas()
for x in range(-300,300):
    for y in range(-300,300):
        if canva.find_overlapping(x*k, y*k,x*k, y*k)==(5,):
            cnt=cnt+1
print(cnt)
done()