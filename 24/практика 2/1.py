f=open('Задание 1.txt')

# если  просят макисмум
# n=f.readline()
# n='T'+n+'T'
# maxi=0
# Ts=[index for index,symbol in enumerate(n) if symbol=='T']
# for t_index in range(len(Ts)-212):
#     res=Ts[t_index+212]-Ts[t_index+1]-1
#     maxi=max(maxi,res)
# print(maxi)
# если просят минимум
n=f.readline()
maxi=float('inf')
Ts=[index for index,symbol in enumerate(n) if symbol=='T']
for t_index in range(len(Ts)-209):
    a=Ts[t_index+209]-Ts[t_index]+1
    maxi=min(maxi,a)
print(maxi)