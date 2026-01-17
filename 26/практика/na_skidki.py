f = open("26.1.txt")
kolvo = int(f.readline())
fullsum = sorted([(int(x)) for x in f], reverse=True)
user_sum = sum(fullsum[len(fullsum) // 9 :])
skidka_machine = 0
for index, price in enumerate(fullsum, 1):
    if index % 9 == 0:
        skidka_machine += price
machine_sum = sum(fullsum) - skidka_machine
print(machine_sum)
