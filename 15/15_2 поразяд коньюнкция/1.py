# for A in range(1,1000):
#     a_podoshel=True
#     for x in range(1,1000):
#         if ((x&79 !=0)<= ((x&64==0)<=(x&A!=0)))==0:
#             a_podoshel=False
#             break
#     if a_podoshel:
#         print(A)
#         break

# for A in range(1,1000):
#     for x in range(1,1000):
#         if (((x&14 !=0) and (x&61 !=0))<=((x&A!=0) and (x&78!=0)))==0:
#             break
#     else:
#         print(A)
#         break

# for A in range(1,10_000):
#     for x in range(1,10_000):
#         if (((x&14!=0)or(x&64!=0)) <=((x&23==0) <=(x&A!=0)))==0:
#             break
#     else:
#         print(A)
#         break

for A in range(1,10000):
    for x in range(1,10000):
        if ((x&A!=0)<=((x&21==0)<=(x&66!=0)))==0:break
    else:
        print(A)
