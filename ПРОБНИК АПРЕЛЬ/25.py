import math
res1=[]
def check(n):
    if n >=2 :
        for nat in range(2,int(math.sqrt(n)+1)):
            if n % nat == 0:
                break
        else:
            if ('1' in str(n)) or( '3' in str(n)):
                return True
        return False

for i in range(3_000_000,3_000_000+1_000_000 ):
    num=0
    for del1 in range(2,int(math.sqrt(i)+1)):
        num+=1
        del2 = i/del1
        if check(del2) and check(del1):
            res1.append(del1)
            res1.append(del2)
            break
    if len(res1)==5:
        print(res1[-1])
        break

print(max(res1))