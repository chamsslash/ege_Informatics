# for A in range(10000,0,-1):
#     a_podoshel=True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if (((17*x-3*y+17)!=0) or (A<x)or (A<y))==0:
#                 a_podoshel=False
#                 break
#         if a_podoshel==0:break
#     if a_podoshel:
#         print(A)
#         break

# for A in range(1,10_000):
#     a_podoshel=True
#     for x in range(1,10_000):
#         for y in range(1,10_000):
#             if (((x>=17)or(3*x<y))or (y*x<A))==0:
#                 a_podoshel=False
#                 break
#         if a_podoshel==0:
#             break
#     if a_podoshel:
#         print(A)


# # решение без флага
# for A in range(1,10000):
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if ((y - 13 * x < A) or (x > 88) or (y > 77)) == False:
#                 break
#         if ((y - 13 * x < A) or (x > 88) or (y > 77)) == False:
#             break
#     else:
#         print(A)

# for A in range(10000,0,-1):
#     a_podoshel=True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if (((17*x-3*y+17)!=0) or (A<x)or (A<y))==0:
#                 a_podoshel=False
#                 break
#         if a_podoshel==0:break
#     if a_podoshel:
#         print(A)
#         break

# короткое решение через генереаторы

# for A in range(1,10000):
#     if all([(y+7*x!=36) or (A>(x-2)) or (A<(y+27)) for x in range(1,10000) for y in range(1,10000)]):print(A);break
# немного изм условие
# for A in range(1,10000):
#      if all([((2*x-y<A) or ((x>55) or (y>32))) for x in range(0,1000) for y in range(0,1000)]):
#          print(A)
#          break