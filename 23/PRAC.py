# def t23(start,end):
#     if start>end or start  ==60:
#         return 0
#     if start==end:
#         return 1
#     if start<end:
#         return t23(start+2,end) + t23(start+3,end)+t23(start+4,end)
# print(t23(56,86))


# def t23(start,end):
#     if start<end :return 0
#     if start==end:return 1
#     if start>end:return t23(start-1,end)+t23(start//2,end)+t23(start//3,end)
# print(t23(131,41)*t23(41,3))




# def t23(s,e):
#     if s>e :return 0
#     if s==e :return 1
#     str_s=str(s)
#     if s<e :return t23(s+1,e)+ (t23(int(str_s[0]+str_s[-1]+str_s[1]),e )if str_s[1]<str_s[-1] else t23(10000,e))
# print(t23(106,163))

def t23(s,e):
    if s>e or s==14 or s==18:return 0
    if s==e :return 1
    if s<e :return t23(s+1,e)+t23(s*2,e)+t23(s*3,e)
print(t23(6,48))
# 102-33=79