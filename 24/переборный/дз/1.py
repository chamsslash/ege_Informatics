seventeendigits = "0123456789ABCDEFG"
f=open("дз/Задание 1.txt")
a=f.readline()
buffa = a[0]
res=[]
for i in range(len(a)-1):
    if a[i] in seventeendigits and a[i+1] in seventeendigits:
        buffa += a[i+1]
    else:
        buffa = a[i+1]
    res.append(buffa)
print(len(max(res, key=len)))