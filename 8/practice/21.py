import itertools
cnt=0
for i in itertools.product('АЛГОРИТМ',repeat=7):
    pod=''.join(i)
    if (sum(pod.count(sogl)for sogl in 'ЛГРТМ' ) > sum(pod.count(gl)for gl in 'АОИ' )):
        cnt+=1
print(cnt)