f=open('Задание 4.txt')
files_count,disks_cound=map(int,f.readline().split())
data=[ list(map(int,filik.split()))for filik in f]
disks=[0]*disks_cound
last_used=0
cnt=0
data.sort()
for start,end in data:
    for index in range(len(disks)):
        if disks[index]+1<=start:
            disks[index]=end
            cnt+=1
            last_used=index+1
            break
        else:
            continue

print(cnt,last_used)