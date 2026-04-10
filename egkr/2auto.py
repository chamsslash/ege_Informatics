from itertools import *
def viraj(x,y,z,w):
    return ((w==z) or not((y<=w)) or not(x))
for n in product([0,1],repeat=5):
    tabletis=[(0,0,1,n[0]),(n[1],1,1,n[2]),(0,n[3],n[4],0)]
    if len(set(tabletis))==3:
        for i in permutations('xyzw'):
            if [viraj(**dict(zip(i,tablet)))for tablet in tabletis] == [0,0,0]:
                print(i)