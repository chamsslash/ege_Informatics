# for A in range(1,10_00):
#     for x in range(1,10_00):
#         for y in range(1,10_00):
#             if ((15 * x + y > A) or (x >= 40) or (y >= 80)) == False:
#                 break
#         if ((15 * x + y > A) or (x >= 40) or (y >= 80)) == False:
#             break
#     else:
#         print(A)
#
for A in range(1,10_00):
    fl=True
    for x in range(1,10_00):
        for y in range(1,10_00):
            if ((15 * x + y > A) or (x >= 40) or (y >= 80)) == False:
                fl=False
                break
        if not fl:
            break
    if fl:
        print(A)

