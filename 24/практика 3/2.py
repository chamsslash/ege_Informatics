f=open('24.2.txt')
data=f.readline().strip()

while '000' in data:
    data=data.replace('000','00 00')
res=data.split()
print(len(max(res,key=len)))
