fourteendigits = "0123456789ABCD"
count=0
f=open("дз/Задание 3.txt")
a=[x.strip() for x in f]
def perevod(x,base):
    # res=0
    # flag=-1 
    # for rune in x:
        #  res+=fourteendigits.index(rune)*base**(len(x)+flag) f
        # lag-=1 
    # return res
    return int(x,base)
for uwu in a:
    if all([digit in fourteendigits for digit in uwu]):
        base=max(fourteendigits.index(sym) for sym in uwu)+1
        if  base >=2 and base <=14 and perevod(uwu,base)%15==0:
            count+=1
print(count)