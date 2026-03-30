f=open('Задание 6.txt')
cm_c,pn_c=map(int,f.readline().split())
comms=[]
planes=[]
uletel=[]
for i in range(cm_c):
    comms.append(int(f.readline()))
for plane in f:
    planes.append(int(plane))
comms.sort(reverse=True)
planes.sort(reverse=True)
for c in comms:
    for pl in planes:
        if 2*c<=pl:
            uletel.append(c)
            planes.remove(pl)
            break
print(len(uletel),max(uletel))