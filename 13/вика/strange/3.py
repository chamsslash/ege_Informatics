import ipaddress
res=[]
for count_ed_mask in range(32,1,-1):
    net1=ipaddress.IPv4Network(f'157.220.185.237/{count_ed_mask}',0)
    net2=ipaddress.IPv4Network(f'157.220.184.230/{count_ed_mask}',0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            if f'{ip:b}'.count('1')==15:
                cnt+=1
        res.append(cnt)
print(min(res))