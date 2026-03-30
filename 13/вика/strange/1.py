
from ipaddress import *
ip=ip_address('68.30.20.77')
net_const=''
for k_ones_mask in range(1,33):
    ipnet=ip_network(f'{ip}/{k_ones_mask}',0)
    if f'{ipnet.network_address:b}'.count('1')==32-k_ones_mask:
        net_const=ipnet
        print('network adress',f'{ipnet.network_address}')
print(net_const)
cnt=0

for ip1 in net_const:
    if f'{ip1:b}'.count('1')==10:
        print(ip1)
        cnt+=1
print(cnt)
