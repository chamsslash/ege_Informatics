from itertools import product
cnt=0
for i in (product('123456',repeat=4)):
    sh=''.join(i)
    nechet=len([i for i in sh if i in '135'])
    chet=len([i for i in sh if i in '246'])
    if ((sh.count('3')==1) and (chet<=nechet)):
        cnt+=1
print(cnt)