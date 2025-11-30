from math import *
f=open("27A_1.txt")
f.readline() #скипаем название столбцов
points=[(list(map(float,s.replace(",",".").split()))) for s in f]
clusters = [[],[]] #два внутренних списка это отдельные кластеры
for x,y in points:
    if y>2:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
best_centroids=[[],[]]#центроид первого класета и второго в отдельных вложенных списках
for i in range(len(clusters)):
    min_sum_dist = 10**10
    for c_x,c_y in clusters[i]:
        sum_dist=0 #расстояние между двумя точками
        for p_x,p_y in clusters[i]:
            sum_dist+= dist([c_x,c_y],[p_x,p_y]) #координаты xy точки
        if sum_dist<min_sum_dist:
            min_sum_dist=sum_dist
            best_centroids[i]=[c_x,c_y]
print(best_centroids)
P_X=sum([x for x,y in best_centroids])/len(best_centroids)
P_Y=sum([y for x,y in best_centroids])/len(best_centroids)
print(int(P_X*10000))
print(int(P_Y*10000))