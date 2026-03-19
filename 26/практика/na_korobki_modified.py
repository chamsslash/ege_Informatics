f = open("26.3.txt")
k = f.readline().split()
kolvo_boxes, kolvo_lentochek = int(k[0]), int(k[1])
boxes = []
tapes = []
for _ in range(kolvo_lentochek):
    line = f.readline().split()
    boxes.append(int(line[0]))
    tapes.append(int(line[1]))
for _ in range(kolvo_boxes - kolvo_lentochek):
    x = f.readline().split()
    boxes.append(int(x[0]))
    tapes.append(0)
# paired = list(zip(boxes, tapes))
# paired.sort(reverse=True)
# boxes, tapes = map(list, zip(*paired)) if paired else ([], [])
gift = []
for box in boxes:
    if box in tapes and len(gift) == 0:
        gift.append(box)
    elif box in tapes and gift[-1] - box >= 7:
        gift.append(box)
print(len(gift))
