p=[i/10 for i in range(260,541)]
q=[i/10 for i in range(191,741)]
a=[]
for x in range(0,10_000):
    x=x/10
    if( ( (x in q ) <= (x in p)) or (x in a ))==0:
        a.append(x)
print(a)
print(len(a)/10)
print("ответ мин непрерывный отрезок а покрвывающй два этих отрзка это 19-75 те длиною 55")