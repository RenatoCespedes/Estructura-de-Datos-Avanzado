def printi(arr):
    for i in arr:
        print(i,end=' ')
    print()
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [9,5,1]
printi(arr)
InsertionSort(arr)
printi(arr)
