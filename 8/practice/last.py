from  itertools import  *
cnt=0
for i in product('0123456789ABCDE',repeat=5):
    num=''.join(i)
    if ( (num[0]!='0' )and (num.count('8') ==1 )and sum(num.count(d) for d in 'ABCDE')>=2):
        cnt+=1
print(cnt)
