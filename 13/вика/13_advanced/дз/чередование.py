from ipaddress import ip_network

net = ip_network("111.1.234.205/255.255.248.0", 0)
cnt = 0

for ip_addr in net:

    a = str(ip_addr).split('.')

    z0 = bin(int(a[0]))[2:].zfill(8).count('0') % 2
    z1 = bin(int(a[1]))[2:].zfill(8).count('0') % 2
    z2 = bin(int(a[2]))[2:].zfill(8).count('0') % 2
    z3 = bin(int(a[3]))[2:].zfill(8).count('0') % 2


    # первый не равен второму, второй не третьему, третий не четвертому
    if (z0 != z1) and (z1 != z2) and (z2 != z3):
        cnt += 1

print(cnt)
# octets = [f"{int(x):08b}" for x in str(ip).split('.')]
# zeros = [o.count('0') % 2 for o in octets]
# if zeros == [0, 1, 0, 1] or zeros == [1, 0, 1, 0]: