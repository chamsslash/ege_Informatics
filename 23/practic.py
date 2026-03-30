# def t23(s,e,k):
#     if s>e:
#         return 0
#     if s==e and k.count('*')==2:
#         return 1
#     if s<e:return t23(s+2,e,k+'+')+t23(s+3,e,k+'+')+t23(s*2,e,k+'*')+t23(s*3,e,k+'*')
#     else:return 0
# print(t23(1,51,''))
# def t23(s,e,k):
#     if s<e:return t23(s+1,e,k+'+')+t23(s*3,e,k+'*')
#     if ((s==e) and ('++++' not in k )and ('****' not in k)):return 1
#     else: return 0
# print(t23(1,30,''))
