f=open('Задание 7.txt')
def prime(n):
    return all(n%i!=0 for i in range(2,(int(n**(0.5))+1)))
box_c=int(f.readline())
boxes=[]
for box in f:
    boxes.append(int(box))
boxes.sort(reverse=True)
gift=[]
for boxoo in boxes:
    if  prime(boxoo) and len(gift)==0:
        gift=[boxoo]
    if prime(boxoo) and gift[-1]-boxoo>=8:
        gift.append(boxoo)
print(len(gift))
print(min(gift))