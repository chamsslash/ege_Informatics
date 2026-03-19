f=open('task1.txt')
kolvo_zanatih,kolvo_ryads,kolvo_mest=map(int,f.readline().split())
aval_place=[]
# считываем занимание мест
mesta=[kolvo_ryads]*(kolvo_mest+1)
for visit in f:
    ryad,mesto=map(int,visit.split())
    mesta[mesto]=min(mesta[mesto],(ryad-1))
for mest_num in range(1,len(mesta)-1):
    min_av_pair=min(mesta[mest_num],mesta[mest_num+1])
    aval_place.append([min_av_pair,mest_num,mest_num+1])
print(aval_place)
print(max(aval_place))