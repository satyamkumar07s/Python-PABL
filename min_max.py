arr = [1, 4, 3, 5, 8, 6]

min = arr[0]
max = arr[0]

for x in arr:
    if x < min:
        min = x
    if x > max:
        max = x

print([min, max])
