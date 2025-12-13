# def Del(n,m):
#     return n%m == 0
# for a in range(1,10000):
#     if all([((Del(x,a))<=(not(Del(x,18)) or Del(x,72)))  for x in range(1,1000)]):
#         print(a)
def Del(n, m):
    return n % m == 0

for a in range(1,10000):
    if all([ (Del(x,a) <= ((not Del(x,18)) or Del(x,72))) for x in range(1,1000) ]):
        print(a)
        break
