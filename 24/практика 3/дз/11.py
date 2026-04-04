f=open('Задание 11.txt')
chunks=f.readline().strip()
while 'MU'  in chunks or 'UM' in chunks:
    chunks=chunks.replace('MU','M U').replace('UM','U M')

chunks=chunks.split()
print(len(max(chunks,key=len)))