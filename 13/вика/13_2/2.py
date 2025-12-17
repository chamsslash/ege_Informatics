from ipaddress import ip_network
for a in range(256):
    net=ip_network(f'127.254.{a}.19/255.255.224.0',0)
    for ip in net:
        if (f'{ip:b}'[:16].count('1')>=f'{ip:b}'[16:].count('1'))==False:
            break
    else:
        print(a)