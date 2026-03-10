alph='1234567890ABCDEFGHIJKLMNOPQRSTUVWXY'
res=[]
for x in alph:
    for y in alph:
        v= int(int(f'32{y}{x}13',35)+ int(f'6{y}{x}25',35))
        if v%47==0:
            break
    else:
        v1 = int(int(f'327{x}13', 35) + int(f'67{x}25', 35))
        res.append(v1//5)
print(max(res))