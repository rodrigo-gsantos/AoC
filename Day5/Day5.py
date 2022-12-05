Stacks = [[],["C", "Z", "N", "B", "M", "W", "Q", "V"],
          ["H", "Z", "R", "W", "C", "B"],
          ["F", "Q", "R", "J"],
          ["Z", "S", "W", "H", "F", "N", "M", "T"],
          ["G", "F", "W", "L", "N", "Q", "P"],
          ["L", "P", "W"],
          ["V", "B", "D", "R", "G", "C", "Q", "J"],
          ["Z", "Q", "N", "B", "W"],
          ["H", "L", "F", "C", "G", "T", "J"]]

X = [l.strip().split(" ") for l in open("Day5Input.txt")]

'''Part 1'''

for el in X:
    j = int(el[1])
    i = 0
    toRemove = int(el[3])
    toAdd = int(el[5])
    while i < j:
        lastItem = Stacks[toRemove].pop()
        Stacks[toAdd].append(lastItem)
        i += 1

i = 1
while i < len(Stacks):
    print(Stacks[i][-1])
    i += 1

'''Part 2'''

Stacks2 = [[],["C", "Z", "N", "B", "M", "W", "Q", "V"],
          ["H", "Z", "R", "W", "C", "B"],
          ["F", "Q", "R", "J"],
          ["Z", "S", "W", "H", "F", "N", "M", "T"],
          ["G", "F", "W", "L", "N", "Q", "P"],
          ["L", "P", "W"],
          ["V", "B", "D", "R", "G", "C", "Q", "J"],
          ["Z", "Q", "N", "B", "W"],
          ["H", "L", "F", "C", "G", "T", "J"]]

X2 = [l.strip().split(" ") for l in open("Day5Input.txt")]

print("====SEPARATION====")

for el in X2:
    i = int(el[1])
    toRemove = int(el[3])
    toAdd = int(el[5])
    while i != 0:
        lastItem = Stacks2[toRemove][-i]
        Stacks2[toRemove].pop(len(Stacks2[toRemove]) - i)
        Stacks2[toAdd].append(lastItem)
        i -= 1

i = 1
while i < len(Stacks2):
    print(Stacks2[i][-1])
    i += 1