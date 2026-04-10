from http.cookiejar import FileCookieJar
res=[]
f=open('24_4.txt')
data=f.readline()
for l in range(len(data)):
    cnt=0
    if not data[l].isdigit():
        for j in range(l+1,len(data)):
            if data[j]==data[l]:
                res.append([len(data[l:j+1]),-l])
            if not(data[j].isdigit()):
                break
res.sort(reverse=True)

print((res[:5]))

