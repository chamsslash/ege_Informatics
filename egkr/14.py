from string import printable

o1=2*2187**567+729**566-2*243**565+81**564-2*27**563-6561
alph=printable[:27]
def to27(n):
    res=''
    while n:
        res+=str(alph[n%27])
        n//=27
    return res[::-1]
o1_27=to27(o1)
gpt=sum([1 for ch in o1_27 if ch in printable[10:27]])
print(gpt)