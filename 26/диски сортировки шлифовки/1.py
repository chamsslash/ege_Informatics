from operator import indexOf

f=open("26.1.txt")
cnt=0
disk_num=0
disk_count=int(f.readline())
files_count=int(f.readline())
files=[[int(x.split()[0]),int(x.split()[1])] for x in f]
files.sort()
disks=[0]*disk_count
for s,end in files:
    for disk_index in range(len(disks)):
        if int(disks[disk_index])<int(s):
            disks[disk_index]=end
            cnt=cnt+1
            disk_num=disk_index
            break
print(cnt,disk_num+1)