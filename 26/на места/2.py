# если бы надо было свободных в общем в ряду даже с разрывами
# f=open('test.txt')
# zanat_c,ryads_c,mest_v_ryadu=map(int,f.readline().split())
# svobodi=[]
# # границы
# bron=[[] for _ in range(mest_v_ryadu+1)]
# for z in f:
#     ryad,mesto=map(int,z.split())
#     bron[mesto].append(ryad)
#
# for ryads in (bron):
#     if len(ryads)!=0:
#         ryads.append(0)
#         ryads.append((ryads_c + 1))
#         max_svob_num = 0
#         print(sorted(ryads,reverse=True))
#         ryads.sort(reverse=True)
#         for z1 in range(len(ryads)-1):
#             if (ryads[z1] - (ryads[z1+1]))>1:
#                 max_svob_num= ryads[z1]-1
#         # [6, 5,4,3  0]
#         if max_svob_num>0:
#             kolvo_svobodn=max(ryads)-min(ryads)-1-(len(ryads)-1)-1
#             svobodi.append([kolvo_svobodn,max_svob_num])
# print(max(sorted(svobodi,reverse=True)))
# print(svobodi)


f = open("Задание 2.txt")
n, m, k = map(int, f.readline().split())

mesta = [[] for i in range(k + 1)]

for s in f:
    ryad, place = map(int, s.split())
    mesta[place].append(ryad)

res = []

for i in range(1, len(mesta)):
    mesta[i] = sorted([0] + mesta[i] + [m + 1], reverse=True)

    for j in range(len(mesta[i]) - 1):
        up, down = mesta[i][j], mesta[i][j + 1]
        # перебираем вообще все во
        res.append([up - down - 1 - 1, up - 1])

res.sort(reverse=True)
print(res)
print(max(res))
