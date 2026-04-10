f=open("9.txt")
cnt=0
data=[list(map(int,i.split())) for i in f]
for stroka in data:
    stroka.sort(reverse=True)
    if (max(stroka)<(sum(stroka)-max(stroka))):
        if (stroka[0]+stroka[-1]) != (stroka[1]+stroka[2]):
            cnt+=1
print(cnt)