f = open("26.2.txt")
kolvo = int(f.readline())
boxes = [int(x) for x in f]
boxes.sort(reverse=True)
gifts = [boxes[0]]
for box in boxes:
    if gifts[-1] - box >= 9:
        gifts.append(box)
print(len(gifts), min(gifts))
