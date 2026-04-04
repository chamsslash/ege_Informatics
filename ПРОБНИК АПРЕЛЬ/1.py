from itertools import permutations

lets=[['АБ'],['АЕ'],['АГ'],['БГ'],['БВ'],['ВД'],['ВИ'],['ИЖ'],['ДЖ'],['ЖЕ'],['ГЕ'],['БЕ']]
print(len(lets))
nums=[[1,3],[1,5],[1,7],[2,4],[2,5],[2,6],[3,8],[4,6],[4,7],[4,8],[5,6],[7,8]]

print(len(nums))
for i in permutations('АБВГДЕЖИ'):
    if all((([i[p1-1]+i[p2-1]] in lets)  or ([i[p2-1]+i[p1-1]] in lets) )for p1,p2 in nums):

        print(i)