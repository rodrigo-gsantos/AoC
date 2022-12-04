X = [l.strip() for l in open("Day3Input.txt")]
points = 0
score = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26,
         'A': 27,'B': 28,'C': 29,'D': 30,'E': 31,'F': 32,'G': 33,'H': 34,'I': 35,'J': 36,'K': 37,'L': 38,'M': 39,'N': 40,'O': 41,'P': 42,'Q': 43,'R': 44,'S': 45,'T': 46,'U': 47,'V': 48,'W': 49,'X': 50,'Y': 51,'Z': 52}
alreadySeen = []

'''Part1'''
for j in X:
    first = j[0:(len(j)//2)]
    second = j[(len(j)//2):len(j)]
    alreadySeen = []
    for char in first:
        if char in second and char not in alreadySeen:
            points += score[char]
        if char not in alreadySeen:
            alreadySeen.append(char)
print("Points: " + str(points))

'''Part2'''

count = 0
points2 = 0
while count < len(X):
    first = X[count]
    second = X[count+1]
    third = X[count+2]
    alreadySeen = []
    for char in first:
        if char in second and char in third and char not in alreadySeen:
            points2 += score[char]
        if char not in alreadySeen:
            alreadySeen.append(char)
    count += 3
print("Points2: " + str(points2))