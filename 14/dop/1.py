alph=("012345678")
for x in alph:
    a=int(f'2{x}{x}86',9) + int(f'72{x}38',9)
    if a % 14==0:
        print(x,a//14)