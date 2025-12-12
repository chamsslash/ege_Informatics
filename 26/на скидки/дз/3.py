f=open("Задание 3.txt")
n=int(f.readline())
a=[int(x) for x in f ]
a.sort(reverse=True)
b=a[:len(a)//3]

print(sum(a)-sum(b))
sale2=0
for i in range(n):
    if (i+1)%3==0:
        sale2+=a[i]
print(sum(a)-sale2)