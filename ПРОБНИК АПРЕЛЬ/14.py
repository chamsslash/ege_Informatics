from string import printable

o1=2187**900 + 4 * 729**900 - 2 * 27**900 - 13122
alph=printable[:27]
def to_27(n):

    res=''
    while n:
        res+=str(alph[n%27])
        n//=27
    return res[::-1]
o1_27=to_27(o1)
schet=sum([1 for digit in o1_27 if digit in printable[11:]])
print(schet)
