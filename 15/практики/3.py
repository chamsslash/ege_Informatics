for A in range(10_000,0,-1):
    for x in range(1,10_000):
        for y in range(1,10_000):
            if ((x+y<=30) or (y<=x-5) or (y>=A))==0:
                break

        if ((x+y<=30) or (y<=x-5) or (y>=A))==0:
                break
    else:
        print(A)
# for A in range(10_000,0,-1):
#     fl=True
#     for x in range(1,10_000):
#         for y in range(1,10_000):
#             if ((x+y<=30) or (y<=x-5) or (y>=A))==0:
#                 fl=False
#                 break
#         if not fl:
#             break
#     if fl:
#         print(A)
