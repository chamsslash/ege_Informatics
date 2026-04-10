from  ipaddress import *
res=[]
for A in range(253):

    net=ip_network(f'64.129.{A}.10/255.255.252.0',0)
    for ip in net:
        ip2=f'{ip:b}'.zfill(32)
        f_half=ip2[:16]
        sec_half=ip2[16:]
        if (f_half.count('1')<=sec_half.count('1'))==0:
            break
    else:
        res.append(A)
print(min(res))