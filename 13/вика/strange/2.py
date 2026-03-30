import ipaddress
cnt=0
ip=ipaddress.IPv4Address('169.25.132.59')
for k_edinic_mask in range(1,33):
    net=ipaddress.IPv4Network(f'{ip}/{k_edinic_mask}',strict=False)
    if f'{net.network_address:b}'.count('1') == 32-k_edinic_mask:
        for ip1 in net:
            ip1_str=f'{ip1:b}'
            if ip1_str.count('1') == 11:
                cnt+=1
print(cnt)
