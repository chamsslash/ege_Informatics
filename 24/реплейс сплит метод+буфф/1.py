f = open("24.1.txt")
s = f.readline()
s = s.replace("-", "*")
chunks = s.split("*")
max_chunk = ""
chunk_loader = ""
# '123*912*0192'
for chunk in chunks:
    if len(chunk) > 0 and chunk[0] != "0":
        chunk_loader += chunk + "*"
    elif len(chunk) > 1 and chunk[0] == "0":
        # 01234
        chunk_loader = str(int(chunk)) + "*"
        # по факту сразу инициализируем новый чанк(откидывая ведущие нули) для чанк лодера
    else:
        # если одиночный ноль стоит то так и будет
        chunk_loader = ""
    max_chunk = max(max_chunk, chunk_loader, key=len)

print(max_chunk)
print(len(max_chunk) - 1)
