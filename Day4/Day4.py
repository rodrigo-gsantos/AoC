X = [l.strip().split(",") for l in open("Day4Input.txt")]

'''Part 1'''
count = 0
for el in X:
    firstInterval = el[0].split("-")
    secondInterval = el[1].split("-")
    if((int(firstInterval[0]) <= int(secondInterval[0]) and int(firstInterval[1]) >= int(secondInterval[1]))
    or (int(secondInterval[0]) <= int(firstInterval[0]) and int(secondInterval[1]) >= int(firstInterval[1]))):
        count += 1
print(count)

'''Part 2'''
count2 = 0
for el in X:
    firstInterval = el[0].split("-")
    secondInterval = el[1].split("-")
    array = []
    array2 = []
    i = int(firstInterval[0])
    j = int(secondInterval[0])
    while i <= int(firstInterval[1]):
        array.append(i)
        i+=1
    while j <= int(secondInterval[1]):
        array2.append(j)
        j+=1
    for i in array:
        if i in array2:
            count2 += 1
            break;
print(count2)