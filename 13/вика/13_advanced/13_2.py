from ipaddress import *

for i in range(32,16,-1):
    net=ip_network(f'121.96.174.205/{i}',0)
    cnt = 0
    for ip in net:
        if f'{ip:b}'.count('1')==12:
            cnt+=1

    if cnt ==10:
        print(i)