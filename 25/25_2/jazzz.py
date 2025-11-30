def dima_prime(n):
    for d in range(2,int((n**0.5))+1):
        if n%d == 0:
            return False
    return n>1

for svarka in range(6_651_221,6_651_220+10000):
    for detka in range(2,int(svarka**0.5)+1):
        if svarka%detka==0:
            if (dima_prime(detka) and dima_prime(svarka//detka)) and (str(detka).count('2')==1 and str(svarka//detka).count('2')==1):

                print(svarka, max(detka, svarka//detka))
                break

#
# 6651241 2579
# 6651262 3325631
# 6651286 3325643
# 6651314 3325657
# 6651347 289189