import math

# f=350301
# res=[]
# while len(res)!=6:
#     dels=[]
#     for delit in range(2,int(math.sqrt(f))+1):
#
#         if f%delit==0:
#             dels.append(delit)
#             dels.append(f//delit)
#     if sum(dels)%13==0:
#         res.append([f,sum(dels)])
#     f+=1
# for chislo,sumdels in res:
#     print(chislo,  sumdels//13)

res=[]
# попробую переписал на цикл фор
for f in range(500_001,500_001+10000):
    if len(res)==5:
        break
    dels=[]
    for delitel in range(18,f,10):
        if f%delitel==0 and str(delitel)[-1]=="8":
            res.append([f,delitel])
            break
for i in res:
    print(i[0],i[1])


