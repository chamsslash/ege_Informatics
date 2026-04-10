from ipaddress import *
res=[]
net=ip_network('146.180.173.153/255.192.0.0',0)
for ip in net:
    res.append((ip))
res.sort(reverse=True)
print(res[:5])