f=open('Задание 5.txt')
com_c,plane_c=map(int,f.readline().split())
commands=[]
planes=[]
for i in range(com_c):
    command=int(f.readline())
    commands.append(command)
for plane in f:
    planes.append(int(plane))
commands.sort(reverse=True)
planes.sort(reverse=True)
uletel=[]
for com in commands:
    for plan in planes:
        if com<=plan:
            uletel.append(com)
            planes.remove(plan)
            break
print(len(uletel),max(uletel))
