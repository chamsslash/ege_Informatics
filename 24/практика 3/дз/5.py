f=open('Задание 5.txt')
data=f.readline().strip()
data='L'+data+'L'
res=[]
lindexes=[ i for i in range(len(data)) if data[i]=='L']
for i in range(len(lindexes)-100):
    o1=lindexes[i+100]-lindexes[i]-1
    res.append(o1)
print(max(res))