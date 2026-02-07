f=open('Задание 4.txt')
n=f.readline().replace('AC','U')
maxi=float('inf')
us=[ i for i,u in enumerate(n) if u =='U']
 # реплейснул
for u_ind in range(len(us)-24):
    a=us[u_ind+24]-us[u_ind]+25+1
    maxi=min(a,maxi)
print(maxi)