from ipaddress import ip_network

for maska in range(16,32+1):
    cnt=0
    net1=ip_network(f"114.75.41.39/{maska}",0)
    net2=ip_network(f"114.75.11.61/{maska}",0)
    if net1==net2:
        print(net2.num_addresses//2)
       # for ip in net1:
       #     if f'{ip:b}'.count('1')%2==0:
       #         cnt += 1
       # print(cnt)