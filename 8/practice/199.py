import itertools
cnt=0
for i in set(itertools.permutations('ВАРЕНЬЕ',r=5)):
    pod=''.join(i)
    if (all((f'{let}{let}'not in pod)for let in 'ВАРЕНЬЕ')):
        cnt+=1
print(cnt)