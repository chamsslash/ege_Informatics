for n in range(0,200):
    n2=bin(n)[2:]
    n2=n2[::-1]

    n10=int(n2,2)
    if n10==43:
        print(n)
#
#
# for n in range(0,200):
#     n2=bin(n)[2:]
#     n2=n2[::-1]
#     n2=n2.lstrip('0') or '0'
#     n10=int(n2,2)
#     if n10==43:
#         print(n)
#         break