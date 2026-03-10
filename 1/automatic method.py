# letts=[['АГ'],['АД'],['ГД'],['ДЕ'],['ЕБ'],['ЕК'],['КБ'],['БВ']]
# nums=[[1,2],[1,7],[2,7],[3,5],[3,6],[4,6],[5,6],[5,7]]
# from itertools import permutations
# for i in permutations("АБВГДЕК"):
#     if all((([i[p1-1]+i[p2-1]] in letts)or ([i[p2-1]+i[p1-1]] in letts)) for p1,p2 in nums ) :
#         print(i)
from itertools import permutations
from sys import setrecursionlimit

lets=[['БА'],['БД'],['АВ'],['ДВ'],['ВК'],['ВГ'],['ВЕ'],['ЕГ']]
nums=[[1,2],[1,4],[2,3],[2,5],[2,6],[2,7],[3,6],[4,5]]
for i in permutations('АБВГДЕК'):
    if all((([i[p1-1]+i[p2-1]] in lets) or ([i[p2-1]+i[p1-1]] in lets)) for p1,p2 in nums):
        print(i)