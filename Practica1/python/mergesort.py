#import random

def mergeSort(arr): 
    if len(arr) >1: 
        m = len(arr)//2 
        L = arr[:m]  
        R = arr[m:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

print("Merge Loaded")

"""n = int(input())
print(n)

arr = [0]*n

for i in range(n):
	arr[i] = random.randint(0,n)

print('Arreglo sin ordenar: ')
print(arr)
mergeSort(arr)
print('Arreglo ordenado por Quicksort: ')
print(arr)"""
