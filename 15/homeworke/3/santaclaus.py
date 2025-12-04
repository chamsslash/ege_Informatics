# for A in range(1,10000):
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if (((y+10*x!=28) or (A>x-1)) and (A<y+50))==0:
#                 break
#         if (((y + 10 * x != 28) or (A > x - 1)) and (A < y + 50)) == 0:
#             break
#     else:
#         print(A)
#         break
#
# for A in range(10_000,0,-1):
#     for x in range(1,10_00):
#         for y in range(1,10_00):
#             if (((15*x-y+40)!=0)or(A<x)or(A<y))==0:
#                 break
#         if (((15 * x -y + 40) != 0) or (A < x) or (A < y)) == 0:
#             break
#     else:
#         print(A)
cnt=0
for A in range(0,1000):
    if all((((x>15)<=(x*y+10*x>=A))and((y*x+y>A)<=(y>=1)))for x in range(0,1000) for y in range(0,1000)):cnt+=1
print(cnt)
