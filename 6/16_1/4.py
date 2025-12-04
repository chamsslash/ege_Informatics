from turtle import *
k=5
tracer(0)
cnt=0
left(90)
pendown()
begin_fill()
for z in range(2):
    right(90)
    forward(120*k)
    right(90)
    forward(14 * k)
end_fill()
canva=getcanvas()
for x in range(-2000,2000):
    for y in range(-2000,2000):
        if canva.find_overlapping(x*k, y*k,x*k, y*k) != ():
            cnt=cnt+1
penup()
print(cnt)
done()
# включительно границы по условию