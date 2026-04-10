f=open('Задание 4.txt')
data=f.readline()
res=[]
for  i in range(len(data)):
    if not data[i].isdigit():
        for j in range(i+1,len(data)):
            if data[j] == data[i]:
                res.append([len(data[i:j+1]),-i])
            if not data[j].isdigit():
                break
print(max(res))