import random

a = ["b","a","s","t","o"]

c = ["t","x","t","b","a"]

matching = []

for i in range(5):
    for element_c in c:
        if element_c in a and element_c not in matching:
            matching.append(element_c)

random.shuffle(matching)
print(matching)