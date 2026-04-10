f=open('24.3.txt')
data=f.readline().strip()
while ('12' in data) or ('21' in data):
         data=data.replace('12','1 2').replace('21','2 1')
res=data.split()
print(len(max(res,key=len)))

