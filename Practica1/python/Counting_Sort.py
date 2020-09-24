def countingSort(data):
    counts = [0 for i in range(max(data)+1)]

    for el in data:
        counts[el] += 1 

    for index in range(1, len(counts)):
        counts[index] = counts[index-1] + counts[index]

    L = [0 for loop in range(len(data))]
    for el in data:
        index = counts[el] - 1
        L[index] = el
        counts[el] -= 1 

	return L

print("Counting Loaded")
"""data = [4, 2, 2, 8, 3, 3, 1]
print("Array antes del cambio")
print(data)
countingSort(data)
print("Aplicando Counting Sort ")
print(data)"""
