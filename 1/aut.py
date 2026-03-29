lets=[['AD'],['BD'],['CF'],['DG'],['DF'],['EG'],['HG'],['AB'],['BE'],['EH'],['HC'],['CA']]
print(len(lets))
nums=[[1,2],[1,3],[1,4],[1,7],[2,6],[3,5],[3,8],[4,5],[4,7],[5,8],[6,7],[6,8]]
print(len(nums))
from itertools import permutations
for i in permutations('ABCDEFGH'):
    if all((([i[p1-1]+i[p2-1]] in lets)  or ([i[p2-1]+i[p1-1]] in lets) )for p1,p2 in nums):
        print(i)