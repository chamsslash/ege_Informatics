# from turtle import *
# k=30
# pendown()
# screensize(2000,2000)
# pendown()
# for i in range(123):
#     forward(10*k)
#     right(120)
# penup()
# for x in range(-20,20):
#     for y in range(-20,20):
#         setpos(x*k,y*k)
#         dot()
#
# done()
cnt=0
from  math import *
for x in range(-1000,1000):
    for y in range(-1000,1000):
        if y<0 and x>0 and y>(tan(radians(120)))*x and y >( tan(radians(60))*x -(111 * sqrt(3))):
            cnt+=1
print(cnt)

# cnt = 0
# for x in range(0, 200):
# for y in range(0, 200):
# if x> 0 and y > tan(radians(30)) * x and y < tan(radians(150))* x + 111:
# cnt += 1
# print(cnt)