# import string
# from string import printable
#
# f=open('Задание 1.txt')
# data=f.readline().strip()
# digits=string.digits
# lets=string.ascii_uppercase
# alph_22=string.digits+string.ascii_uppercase[:12]
# def is_aval_to_conc(buff,new_char):
#     if ((new_char in alph_22) and (((buff[-1] in digits) and (new_char not in digits) )
#                                      or ((buff[-1] in lets) and (new_char not in lets)))):
#         return True
#     else:
#         return False
#
# resbuff=[]
# buff=''
# for i in data:
#     if ((len(buff)==0) and i in (alph_22[1:])):
#         buff=i
#     elif ((len(buff)>0) and (i in alph_22)) and is_aval_to_conc(buff,i):
#             buff+=i
#     else:
#         resbuff.append(buff)
#         if i in alph_22[1:]:
#             buff=i
#         else:
#             buff=''
#
# resbuff.append(buff)
#
# print(max(resbuff,key=len))
# print(len(max(resbuff,key=len)))
#
import string
from re import*
alph_22=string.digits+string.ascii_uppercase[:12]
print(alph_22)
f=open('Задание 1.txt')
data=f.readline().strip()
valid=findall(r'[123456789]?(?:[ABCDEFGHIJKL][0123456789])+[ABCDEFGHIJKL]?',data)
print(max(valid,key=len))
print(len(max(valid,key=len)))