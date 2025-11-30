def dima_prime(n):
    for d in range(2,int((n**0.5))+1):
        if n%d == 0:
            return False
    return n>1
for n in range(5_400_001,5_400_001+10000):
    dels=[]
    M=0
    for d in range(2,int(n**0.5)+1):
        if (n%d==0 ):
            if dima_prime(d):
                dels.append(d)
            if dima_prime(n//d):
                dels.append(n//d)
    dels=list(set(dels))
    if len(dels)>0:
        M=max(dels)+min(dels)
        if M>60_000 and (str(M) ==  str(M)[::-1]):
            print(n,M)