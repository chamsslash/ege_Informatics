f=open('Задание 2.txt')
data=f.readline().strip().replace('000','00 00')
data_1=data.split()
print(len(max(data_1,key=len)))