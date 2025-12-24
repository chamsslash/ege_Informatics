f=open('26.1.txt')
cnt=0
last_disk=0
disks_count=int(f.readline())
files_count=int(f.readline())

files=[[int(x.split()[0]),int(x.split()[1])]for x in f]
files.sort()
all_disks=[0]*disks_count
for s,e in files:
    for i in range(disks_count):
        if int(all_disks[i])<int(s):
            all_disks[i]=e
            cnt+=1
            last_disk=i
            break
print(cnt,last_disk+1)