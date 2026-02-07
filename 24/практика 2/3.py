f=open("Задание 3.txt")
n=f.readline().replace('DE','Z')
maxi=0
n='Z'+n+'Z'
zs=[i for i,z in enumerate(n) if z =='Z']
for z_index in range(len(zs)-151):
    a=zs[z_index+151]-zs[z_index]+152-1
    maxi=max(maxi,a)
print(maxi)
