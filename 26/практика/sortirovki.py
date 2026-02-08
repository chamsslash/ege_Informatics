f=open('26.5.txt')
k=int(f.readline())
n=int(f.readline())
last_box_num=0
count=0
data=[]
boxes=[0]*k
for s in f:
    start,end=map(int,s.split())
    data.append((start,end))
data.sort()
for start,end in data:
    for num_box in range(k):

        # ячейка освобождается на свлед минуту только
        if boxes[num_box]+1<start:
            boxes[num_box]=end
            last_box_num=num_box
            count+=1
            break
print(count,last_box_num+1)
