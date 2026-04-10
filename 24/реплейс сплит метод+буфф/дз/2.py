f=open("Задание 2.txt")
f=f.readline()
f=f.replace("-","*").replace("+","*")
chunks=f.split('*')
max_chunks=""
loader=''
for x in chunks:
    if len(x)>1 and x[0]!='0':
        loader+=x+'*'
    elif x == "0":
        loader += '0*'
    elif len(x)>1 and x[0]=='0':
        loader+="0*"
        max_chunks=max(max_chunks,loader,key=len)
        loader = str(int(x))+'*'
    else:
        loader=""
    max_chunks=max(max_chunks,loader,key=len)
print(max_chunks)
print(len(max_chunks)-1)
