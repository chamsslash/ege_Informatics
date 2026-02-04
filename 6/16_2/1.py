from turtle import *

pendown()
k = 20
cnt = 0
begin_fill()
for _ in range(6):
    forward(3 * k)
    left(60)
end_fill()
canvas = getcanvas()

for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            cnt += 1

print(cnt)
done()
