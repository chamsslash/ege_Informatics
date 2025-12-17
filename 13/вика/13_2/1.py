from ipaddress import *
for N in range(9):
# берем октет
    a= int((N*'1')+('0'*(8-N)),2)
    net=ip_network(f'255.224.33.160/255.255.{a}.0',0)
    for ip in net:
        if (f'{ip:b}'[:16].count('1') >= f'{ip:b}'[16:].count('1'))==False:
            break
    else:print(a)