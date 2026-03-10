def Del(x,y):
    return x%y==0
p=list(range(26,53+1))
a=[]
for x in range(1,10_00):
    if ((x in p) <=  ((Del(x,14)) <= (x in a)))==0:
        a.append(x)
print(a)
print('ответ 14')