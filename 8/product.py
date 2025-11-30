from itertools import *
# Numb=1
# for i in product("АДИН",repeat=5):
#     res=''.join(i)
#     if res == "ДИАНА":
#         print(Numb)
#     # print(Numb, '-' ,res)
#     Numb+=1
n=1
for i in product("АБВГДЕЖЗИК",repeat=3):
    res=''.join(i)
    if res == "АГА":
        print(n)
    n+=1