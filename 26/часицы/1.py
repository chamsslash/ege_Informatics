# f=open('1.txt')
# p=int(f.readline())
# res=[]
# ryadi_chastic=[[] for i in range(100_001)]
# for i in f:
#     ryad,pos=int(i.split())
#     ryadi_chastic[ryad].append(int(pos))
# for r in ryadi_chastic:
#     r.append(1000_000)
#     r.append(-100_0000)
#     r.sort()
#     if len(r)==0:
#         continue
#     for index_pos in range(1,len(r)-1):
#         isolat = []
#         if ((r[index_pos]-r[index_pos-1]>=500) and (r[index_pos+1]-r[index_pos]>=500)):
#             isolat.append(index_pos)
#         res.append([len(isolat),ryadi_chastic.index(r)])
# res.sort(reverse=True)
# print(res[:5])
# print(max(res))

