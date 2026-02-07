from string import ascii_uppercase
res=[]
alph="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:19]
for x in alph:
    data= int(f'98{x}79641',19)+ int(f'36{x}14',19)+ int(f'73{x}4',19)
    if data%18==0:res.append([x,int(data//18)])
print(max(res))