# f= kft
t=(2*2**23)/(1.5 * 2**13)
f=2*36*1000*24*t*60
for i in range(1,100):
    f1=f*(i/100)
    f_part=f1/270
    if f_part==20*2**23:
        print(1.0 - i/100)