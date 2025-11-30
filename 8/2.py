from itertools import *
# cnt=0
# for i in product(sorted("QWER123"),repeat=5):
#     if (i.count("1")+i.count("2")+i.count("3"))==2:
#         cnt+=1
# print(cnt)
# gl ='АЕО'
# sogl='БНДРЛ'
# cnt=0
# for i in product("БАНДЕРОЛЬ",repeat=7):
#     word = "".join(i)
#     if sum(1 for x in word if x in gl) > sum(1 for x in word if x in sogl):
#         cnt+=1
# print(cnt)
# cnt=0
# for i in set(permutations(sorted("КАРЕТА"),r=4)):
#     word = "".join(i)
#     flag=True
#     for ind in range(len(word)-1):
#         if word[ind] == word[ind + 1]:
#             flag=False
#     if flag:
#         cnt+=1
# print(cnt)
# cnt=0
# bad_pairs = ["03", "23", "43", "63", "83",
#              "30", "32", "34", "36", "38"]
#
# for i in product("012345678", repeat=6):
#     num = ''.join(i)
#     if num[0] != '0' and num.count("3") == 1:
#         # Если ни одной плохой пары нет в числе
#         if not any(pair in num for pair in bad_pairs):
#             cnt += 1
#
# print(cnt)
# cnt=0
# for i in product('0123456',repeat=5):
#     chislo="".join(i)
#     if chislo[0]!="0" and chislo.count("2")==2 and \
#         all(f'{bad}2'not in chislo and f'2{bad}' not in chislo for bad in '135'):
#         cnt+=1
# print(cnt)
