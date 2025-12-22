from ipaddress import ip_network
for A in range(9):
    a=int('1'*A+'0'*(8-A),2)
    net=ip_network(f"255.201.33.160/255.255.{a}.0",0)
    for ip in net:
        if( f'{ip:b}'[:16].count('1')>f'{ip:b}'[16:].count('1'))==0:
            break
    else:
        print(a)
