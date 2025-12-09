f = open("на скидки/26.3.txt")
n = int(f.readline())
a = [int(x)for x in f]
a.sort(reverse=True)
sale1=(sum(a[:n//3]))
print(sum(a)-sale1)
sale2=0
for x in range(n):
    if (x +1) % 3 == 0:
        sale2+=a[x]
print(sum(a)-sale2)
f = open("на скидки/26.2.txt")
