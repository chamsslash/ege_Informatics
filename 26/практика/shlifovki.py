f = open("26.6.txt")
n = int(f.readline())
end = []
beg = []
for x in range(n):
    srokg, haram = map(int, f.readline().split())
    if srokg < haram:
        beg.append([srokg, x + 1])
    elif srokg > haram:
        end.append([haram, x + 1])
print(max(end), max(beg))
print(len(end) - 1)
