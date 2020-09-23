def countingSort(array):
    size = len(array)
    maxim = int(max(array))
    output = [0] * maxim

    
    count = [0] * (maxim+1)

    
    for i in range(0, size):
        count[array[i]] += 1

    
    for i in range(1, maxim+1):
        count[i] += count[i - 1]

    
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    
    for i in range(0, size):
        array[i] = output[i]

print("")
"""data = [4, 2, 2, 8, 3, 3, 1]
print("Array antes del cambio")
print(data)
countingSort(data)
print("Aplicando Counting Sort ")
print(data)"""
