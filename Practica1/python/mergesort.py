<<<<<<< HEAD
import random 
=======
#import random

def mergeSort(arr): 
    if len(arr) >1: 
        m = len(arr)//2 
        L = arr[:m]  
        R = arr[m:] 
  
        mergeSort(L) 
        mergeSort(R) 
>>>>>>> 7530fb5cbc5d61ecedf1f37cad319140f6ca6446
  
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
          
<<<<<<< HEAD
        # if the current element is smaller or equal to pivot, 
        # shift it to the left side of the partition. 
        if arr[j] <= arr[pivot]: 
            arr[i] , arr[j] = arr[j] , arr[i] 
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot] 
    pivot = i - 1
    return (pivot) 

n = int(input())
=======
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

print("Merge Loaded")

"""n = int(input())
>>>>>>> 7530fb5cbc5d61ecedf1f37cad319140f6ca6446
print(n)

arr = [0]*n

for i in range(n):
	arr[i] = random.randint(0,n)

print('Arreglo sin ordenar: ')
print(arr)
quickSort(arr,0,n-1)
print('Arreglo ordenado por Quicksort: ')
<<<<<<< HEAD
print(arr)

=======
print(arr)"""
>>>>>>> 7530fb5cbc5d61ecedf1f37cad319140f6ca6446
