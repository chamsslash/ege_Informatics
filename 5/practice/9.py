for n1 in range(1000,10000):
    digits=[int(d) for d in str(n1)]
    summ=sum(digits)
    m=max(digits)
    n=min(digits)
    p1=summ-m
    p2=summ-n
    l=str(max(p1,p2))+str(min(p1,p2))

    if l =='2013':
        print(n1)