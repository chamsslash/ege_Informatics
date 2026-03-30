from ipaddress import ip_network
for a in range(256):
    net=ip_network(f'127.254.{a}.19/255.255.224.0',0)
    for ip in net:
        print(f"{ip:b}")
        print(len('01111111111111100000000000000000'))
        break
    break
        # if (f'{ip:b}'[:16].count('1')>=f'{ip:b}'[16:].count('1'))==False:
    #     #     break
    # else:
    #     print(a)