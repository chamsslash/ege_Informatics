# f=open('24_1.txt')
# buff=''
# res=[]
# def isaval(x,x1):
#     return(  ( x.isdigit()) and( not x1.isdigit())) or ((x1.isdigit() and not x.isdigit()) )
# data=f.readline()
# for d in data:
#     if ((len(buff)==0) and (d in '123456789ABCDE')):
#         buff=d
#     if len(buff)>0 and (d in '0123456789ABCDE') and isaval(buff[-1],d):
#         buff+=d
#     elif len(buff)>0 and (d in '0123456789ABCDE') :
#         buff=d
#     else:buff=''
#     res.append(buff)
# print(max(res,key=len))
# print(len(max(res,key=len)))
import re

f=open('24_1.txt')
data=f.readline().strip()
from  re import*
valid=findall(r'[1-9]?(?:[ABCDE][0-9])+[ABCDE]?',data)
print(max(valid,key=len))
print(len(max(valid,key=len)))