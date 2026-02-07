f=open("Задание 6.txt")
n=f.readline().strip()
n="X"+n+'X'
maxi=0
xxx=[i for i,x in enumerate(n) if x =='X']
for x_index in range(len(xxx)-60):
    a=xxx[x_index+60]-xxx[x_index]-1
    ish=n[xxx[x_index+1]:xxx[x_index+60]]
    if ish.count('2025')>=101:
        maxi=max(a,maxi)
print(maxi)
