from ipaddress import ip_network
res=[]
for A in range(256):
    for B in range(256):
        network=ip_network(f'196.{A}.{B}.52/255.255.255.248',0)
        for ip in network:
            if( f'{ip:b}'[:16].count('0')>=f'{ip:b}'[16:].count('1'))==0:
                break
        else:
            res.append(A+B)
print(max(res))