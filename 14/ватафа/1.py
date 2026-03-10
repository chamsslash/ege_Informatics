alph='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for osn_alph in range(10,len(alph)+1):
    for x0 in range(0,osn_alph):
        x=alph[x0]
        for y0 in range(0,osn_alph):
            y=alph[y0]
            for z0 in range(0,osn_alph):
                z=alph[z0]
                for w0 in range(0,osn_alph):
                    w=alph[w0]
                    o=int(f'{y}18{x}',osn_alph)+int(f'{w}{y}98',osn_alph)
                    o1=int(f'{x}{x}{z}4{y}',osn_alph)
                    if o==o1:
                        print(int(f'{x}{y}{z}{w}',osn_alph))