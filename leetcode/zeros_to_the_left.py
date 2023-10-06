array = [9, 0, 8, 78, 9, 0, 99, 0, 89]
for a in range(len(array)):
    if array[a] == 0:
        curr = array.pop(a)
        array.insert(0, curr)
print array
