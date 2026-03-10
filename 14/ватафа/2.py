# alph='0123456'
# for i in range(1,7):
#     x=int(alph[i],7)
#     o=4*7**24+6*7**13+5*49**4+2*343**2+10-x
#     ostr=str(o)
#     if ostr.count('6')>ostr.count('0'):
#         print(i)
#         break
def to7(i):
    res=''
    while i!=0:
        res+=str(i%7)
        i//=7
    return res[::-1]
res1=[]
for x in range(1,100_000_000):
    o=4*7**24+6*7**13+5*49**4+2*343**2+10-x
    o7=to7(o)
    o7_str=str(o7)
    if o7_str.count('6')>o7_str.count('0'):
        res1.append(x)
print(min(res1))
