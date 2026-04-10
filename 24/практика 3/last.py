f=open('24.10.txt')
data=f.readline().strip()

data_no_e=data.split('E')

# res=[]
# for chunk in data_no_e:
#     if chunk.count('A')=='700':
#         res.append(len(chunk))
#         continue
#     строка где больше 700а и мы начинаем искать подстроки с 700 и меньше a
#     chunk = 'A'+chunk+'A'
#     ind_A=[i for i in range(len(chunk)) if chunk[i]=='A']
#     for i in range(len(ind_A)-701):
#         o1=ind_A[i+701]-ind_A[i]-1
#         res.append(o1)
# print(max(res))