#
from ipaddress import  *
# net=ip_network('78.34.19.56/255.255.255.254',0)
# for i in net:
#     print(f'{i:b}',f'{bin(int(i))[2:].zfill(32)}')
# c=0
# net=ip_network('172.16.80.0/255.255.248.0')
# for ip_add in net:
#     ip=bin(int(ip_add))[2:].zfill(32)
#     if ip.count('1')%2!=0:
#         c+=1
# print(c)

# макс айди
# from ipaddress import  *
# net=ip_network("11.92.135.56/255.224.0.0",0)
# print(net[-2])
# не берем широко вещательный


from ipaddress import *
for A in range(1,256):
    net=ip_network(f'32.0.{A}.5/255.255.240.0',0)
    for ip in net:
        if (f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('1'))==0:
            break
    else:
        print(A)