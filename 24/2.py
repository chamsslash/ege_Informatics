file = open("24.2.txt")
f=file.readline()
f=f.replace("-","*")
chunks=f.split('*')
max_chunk = ""
chunk_loader = ""
for chunk in chunks:
    if len(chunk) > 0 and chunk[0] != "0":
        chunk_loader += chunk + "*"
    elif chunk=="0":
        chunk_loader += "0*"
    elif len(chunk) > 1 and chunk[0] == "0":
        chunk_loader +='0*'
        max_chunk = max(max_chunk, chunk_loader, key=len)
        chunk_loader = str(int(chunk)) + "*"
    else:
        chunk_loader = ""
    max_chunk = max(max_chunk, chunk_loader, key=len)

print(max_chunk)
print(len(max_chunk) - 1)
