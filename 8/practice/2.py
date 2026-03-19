from itertools import product

print(sum(
    1
    for i in product('123456', repeat=4)
    if i.count('4') == 1
    and sum(i.count(ch) for ch in '246') <= sum(i.count(ch) for ch in '135')
))