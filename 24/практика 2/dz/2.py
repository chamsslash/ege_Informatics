f=open('2.txt')
n=f.readline()
maxi=0
n='O'+n+'O'
os=[i for i,o in enumerate(n) if o == 'O']
for o_index in range(len(os)-151):
    a=os[o_index+151]-os[o_index]-1
    maxi=max(a,maxi)
print(maxi)