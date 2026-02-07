f=open("Задание 1.txt")
f=f.readline()
f=f.replace("-","*").replace("+","*")
chunks=f.split('*')
max_chunks = ""
chunk_loader = ""
for chunk in chunks:
    if len(chunk)>1 and chunk[0] != "0":
       chunk_loader+=chunk+'*'
    elif len(chunk)>1 and chunk[0] =="0":
        chunk_loader=str(int(chunk))+'*'
    else:
        chunk_loader=""
    max_chunks = max(max_chunks, chunk_loader, key=len)
print(max_chunks)
print(len(max_chunks)-1)