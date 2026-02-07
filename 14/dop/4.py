f=4*3125**2019+3*625**2020 - 2 * 125**2021 + 25**2022 - 4 * 5*2023 -2024
def to25(x):
    cnt=0
    while x>0:
        if x%25>10:
            cnt+=1
        x=x//25
    return cnt
print(to25(f))