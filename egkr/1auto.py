import itertools

numis=[[1,4],[1,5],[1,7],[2,3],[2,4],[2,6],[3,4],[5,6],[5,7],[6,7]]
print(len(numis))
letis=['АБ','АВ','БВ','БД','ВЕ','ДГ','ГЕ','ЕК','ДК','КГ']
print(len(letis))
for x in itertools.permutations('АБВГДЕК'):
    if all(( (x[i1-1]+x[i2-1] in letis) or (x[i2-1]+x[i1-1]) in letis)for i1,i2 in numis):
        print(x)
print(len(x))
# ответ 11