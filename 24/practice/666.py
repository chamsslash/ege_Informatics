f=open('Задание 6.txt')
n=f.readline().strip()
maxi=0
ass=[i for i,a in enumerate(n) if a=='A']
for a_index in range(len(ass)-76):
    a=ass[a_index+76]-ass[a_index]-1
    base=n[ass[a_index+1]:ass[a_index+76]]
    if base.count('2026')>=80:
        maxi=max(a,maxi)
print(maxi)