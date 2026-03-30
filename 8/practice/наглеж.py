from itertools import *
cnt=0
for i in permutations('наглеж',r=4):
    word=''.join(i)
    if all(f'{gl}{gl1}' not in word for gl in 'ае' for gl1 in 'ае'):
        cnt+=1
print(cnt)
        