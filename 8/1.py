from itertools import product
# n=1
# cnt=0
# for i in product(sorted("ИНФОРМАТ"),repeat=5):
#     if n%2!=0 and i[0]!="О" and ("".join(i).count("Н")==1 or "".join(i).count("Н")==2):
#         cnt += 1
#         print(i)
#     n += 1
#
# print(cnt)
# num=1
# cnt=0
# for i in product(sorted("ГВАРДИЯ"), repeat=6):
#     word = "".join(i)
#     if word[0]!="Д" and word.count("Р")>=2 and num%2==0:
#         cnt+=1
#         print(word)
#     num+=1
# print(cnt)
# num=1
# for i in product(sorted("ХРУСТ"), repeat=5):
#     word = "".join(i)
#     if "Х" not in word and word.count("У") == 2:
#         print(num)
#     num+=1
num=1
cnt=0
for i in product(sorted("КУСТ"),repeat=5):
    word = "".join(i)
    if word.count("У")==0 and word.count("Т") ==0:
        if "СС" not in word:
            cnt+=1
            print(num)
    num+=1
