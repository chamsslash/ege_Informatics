for jojo in range(800_001,800_001+1000):
    for delka in range(17,jojo,10):
        if jojo%delka== 0:
            print(delka, "--->", jojo)
            break