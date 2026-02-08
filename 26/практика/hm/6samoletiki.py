f=open('Задание 6.txt')
comms_count,planes_count=map(int,f.readline().split())
comms=[]
planes=[]
for _ in range(comms_count):
    comms.append(int(f.readline()))
for _2 in range(planes_count):
    planes.append(int(f.readline()))
uleteli=0
maxplane=max(planes)
planes.sort()
comms.sort()
for commanda in comms:
    for plane in planes[:]:
        if plane >= commanda:
            uleteli+=1
            planes.remove(plane)
        else:
            continue
massive_comm=max([comm for comm in comms if comm<=maxplane])
print(uleteli,massive_comm)
