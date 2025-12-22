from ipaddress import  *
for n in range(0,9):
    A=int(n*'1'+"0"*(8-n),2)
    net= ip_network(f"199.59.129.3/255.255.{A}.0",0)
    for ip in net:
        if ((f'{ip:b}')[16:].count('1')<=(f'{ip:b}'[:16].count('1')))==False:
            break
    else:
        print(n)