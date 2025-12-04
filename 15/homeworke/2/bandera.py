# for A in range(1,10000):
#     for x in range(1,10000):
#         if ((x&15!=0)or(x&34==0)or(x&A!=0))==0:break
#     else:
#         print(A)
#         break
# for A in range(1000,0,-1):
#     for x in range(1,10000):
#         if (((x&46==0)or(x&18==0))<=((x&115!=0)<=(x&A==0)))==0:break
#     else:
#         print(A)
#         break
for A in range(1,10000):
    for x in range(1,1000):
        if ((x&45!=0)<=((x&23==0)<=(x&A!=0)))==0:break
    else:
        print(A)
        break