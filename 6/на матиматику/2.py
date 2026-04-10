from math import *
cnt=0
for x in range(-1000,1000):
    for y in range(-1000,1000):
        if y<-x and y>(x -sqrt(288)) and y> (-x - sqrt(288)) and y<(x+sqrt(288)):
            cnt+=1
print(cnt)
# from math import *
# cnt=0
# for x in range(-1000,1000):
#     for y in range(-1000,1000):
#         if y<-x and y>(x -sqrt(450)) and y> (-x - sqrt(450)) and y<(x+sqrt(450)):
#             cnt+=1
# print(cnt)