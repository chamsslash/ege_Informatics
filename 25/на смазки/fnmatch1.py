from fnmatch import *
# for x in range(61,10**8,61):
#     if fnmatch(str(x), "23456??8") and x % 61==0:
#         print(x,x//61)
# for x in range(0,10**8+1,63):
#      if fnmatch(str(x),"134?3?") and x%63==0:
#          print(x,x//63)
# for uwu in range(0,10**8,2023):
#     if fnmatch(str(uwu),'37*7?') and uwu% 2023==0:
#         print(uwu,uwu//2023)
for x in range(0,10**8,343):
    if fnmatch(str(x),"51?32*8") and x%343 == 0:
        print(x,x//343)