#import random 
  
''' 
The function which implements QuickSort. 
arr :- array to be sorted. 
start :- starting index of the array. 
stop :- ending index of the array. 
'''
def quickSort(arr, inicio , fin): 
    if(inicio < fin): 
          
        pivotdiv = divrand(arr, inicio, fin) 
  
        quickSort(arr , inicio , pivotdiv - 1) 
        quickSort(arr, pivotdiv + 1, fin) 
  
 
def divrand(arr , inicio, fin): 
  
    randpivot = random.randrange(inicio, fin) 
  
    arr[inicio], arr[randpivot] = arr[randpivot], arr[inicio] 
    return dividir(arr, inicio, fin) 
  
def dividir(arr,inicio,fin): 
    pivot = inicio
    i = inicio + 1 
                  
    for j in range(inicio + 1, fin + 1): 
          
        # if the current element is smaller or equal to pivot, 
        # shift it to the left side of the partition. 
        if arr[j] <= arr[pivot]: 
            arr[i] , arr[j] = arr[j] , arr[i] 
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot] 
    pivot = i - 1
    return (pivot) 
print("Quick Loaded")
"""n = int(input())
print(n)

arr = [0]*n

for i in range(n):
	arr[i] = random.randint(0,n)

print('Arreglo sin ordenar: ')
print(arr)
quickSort(arr,0,n-1)
print('Arreglo ordenado por Quicksort: ')
print(arr)"""
