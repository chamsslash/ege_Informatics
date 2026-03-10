# def f(st,hod,end):
#     if st<=25:
#         return hod in end
#     if hod >=max(end):
#         return False
#     sks=[f(st-1,hod+1,end)]
#     if st%2==0:
#         sks.append(f(st/2+1,hod+1,end))
#     else:
#         sks.append(f(st-2,hod+1,end))
#     if st%3==0:
#         sks.append(f(st/3,hod+1,end))
#     else:
#         sks.append(f(st-3,hod+1,end))
#     # проверка на чела которому мы подкручиваем
#     if ((hod+1)%2)==(end[0]%2):
#         return any(sks)
#     else:
#         return all(sks)
# # for r in range(26,10_000):
# #     if f(r,0,[1]):
# #         print(r)
# print(min(rocks for rocks in range(1,10_00) if f(rocks,0,[2]) ))
# print([rocks for rocks in range(1,10_00) if f(rocks,0,[3]) and not f(rocks,0,[1]) ])
# print([rocks for rocks in range(1,10_00) if f(rocks,0,[4]) and not f(rocks,0,[2]) ])
