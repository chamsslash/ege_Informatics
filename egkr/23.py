def F(start,end):
    if ((start==end) ) :return True
    if ((start>end )or (start==7)):return False
    return F(start+1,end) + F(start+3,end)+F(start*2,end)
print(F(2,15)*F(15,25))