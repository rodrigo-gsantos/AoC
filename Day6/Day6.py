X = [l.strip() for l in open("Day6Input.txt")]

'''Part 1'''

count_Marker = 4
count4 = 0
lista4 = []
for ele in X[0]:
    if count4 < 4:
        lista4.append(ele)
        count4 += 1
    else:
        if len(lista4) != len(set(lista4)):
            count_Marker += 1
            del lista4[0]
            lista4.append(ele)
        else:
            break
print(count_Marker)

'''Part 2'''

count_Marker = 14
count14 = 0
lista14 = []
for ele in X[0]:
    if count14 < 14:
        lista14.append(ele)
        count14 += 1
    else:
        if len(lista14) != len(set(lista14)):
            count_Marker += 1
            del lista14[0]
            lista14.append(ele)
        else:
            break
print(count_Marker)