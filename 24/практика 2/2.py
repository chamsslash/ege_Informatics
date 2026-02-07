f=open("Задание 2.txt")
n=f.readline()
n='M'+n +'M'
maxi=0
M_indexes=[ i for i,m in enumerate(n) if m=='M']
for index in range(len(M_indexes)-101):
    a=M_indexes[index+101]-M_indexes[index]-1
    maxi=max(maxi,a)
print(maxi)