a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

union = []

for x in a:
    if x not in union:
        union.append(x)

for x in b:
    if x not in union:
        union.append(x)

print(union)
