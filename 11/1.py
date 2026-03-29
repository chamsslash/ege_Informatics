from math import  *
#
# N=52+10
# i_dla_alph=ceil(log2(N))
# v_parola=ceil(9*i_dla_alph/8)+18
# res=1*2**10/v_parola
#
#
# print(res)

#
# N=52+10+8
# i=ceil(log2(N))
# lichniy=ceil(17*i/8)
# i_p=ceil(log2(1200))
# podrazd=ceil(i_p/8)
# for dop in range(1,10_000):
#     a=lichniy+podrazd+dop
#     if a<=48:
#         print(dop)

#
# N=963+52+10
# i=ceil(log2(N))
# for lens in range(1,10_000):
#     v=ceil(lens*i/8)
#     if 693*(2**10) >= v*2000:
#         print(lens)



for N in range(1,10_000):
    v=ceil(261*ceil(log2(N))/8)
    if 252500*v>=31*2**20:
        print(N)