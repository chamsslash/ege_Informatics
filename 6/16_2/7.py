from turtle import *
cnt=0
k=250
speed(0)
begin_fill()
for _ in range(10):
    forward(k*6)
    right(90)
    forward(10*k)
    right(90)
end_fill()
canvas=getcanvas()
for x in range(-100,100):
    for y in range(-100,100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            cnt += 1
print(cnt)
done()