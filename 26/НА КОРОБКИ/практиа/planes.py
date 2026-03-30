f=open('26.5.txt')
comm_c,plane_c=map(int,f.readline().split())
commandisi=[]
planesi=[]
for i in range(comm_c):
    command=int(f.readline())
    commandisi.append(command)
for i1 in f:
    plane=int(i1)
    planesi.append(plane)
commandisi.sort(reverse=True)
planesi.sort(reverse=True)
ulet=[]
for comm in commandisi:
    for plan in planesi[:]:
        if comm<=plan:
            ulet.append(comm)
            planesi.remove(plan)
            break
print(len(ulet))
print(max(ulet))