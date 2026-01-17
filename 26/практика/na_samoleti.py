f=open("26.4.txt")
k=f.readline().split()
k1_comms=int(k[0])
k2_planes=int(k[1])
commands=sorted([int(f.readline())for x in range(k1_comms)])
planes=sorted([int(f.readline())for x in range(k2_planes)])
res=[]
max_plane=max(planes)
for command in commands:
    for plane in planes[:]:
        if plane>=command:
            res.append(plane)
            planes.remove(plane)
            break
print(len(res))
print(max([comm for comm in commands if comm< max_plane]))