f=open('Задание 10.txt')
res=[]
# надо найти макс лен когда A и F  встр 150 раз те по факту a=f
data=f.readline().strip().replace('F','A')
a_indexes=[i for i in range(len(data)) if data[i]=='A']
for i in range(len(a_indexes)-151):
    o1=a_indexes[i+151]-a_indexes[i]-1
    res.append(o1)
print(max(res))