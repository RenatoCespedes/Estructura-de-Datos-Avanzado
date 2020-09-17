def printi(arr):
    for i in arr:
        print(i,end=' ')
    print()
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j>i:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
arr = [9,5,1]
printi(arr)
BubbleSort(arr)
printi(arr)
