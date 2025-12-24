f=open('26.2.txt')
k=int(f.readline())
details=[[int(d.split()[0]),int(d.split()[1])] for d in f]
shpak=[]
okras=[]
for index in range(len(details)):
    index1=index+1
    s=details[index][0]
    o=details[index][1]
    if s<o:
        shpak.append([s,index1])
    else:
        okras.append([s,index1])
shpak.sort()
okras.sort()
print(max(shpak),len(shpak)-1)