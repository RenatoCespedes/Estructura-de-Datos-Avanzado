import random
"""
def swap(a,b):
	t = a;
	a = b;
	b = t;
	return a,b"""


def dividir(arr,inicio,fin):
	pivot = arr[fin]
	x = inicio-1
	
	for i in range(inicio,fin):
		if arr[i]<pivot:
			x=x+1
			arr[x], arr[i] = arr[i], arr[x]
	
	arr[x+1],arr[fin] = arr[fin], arr[x+1]
	return (x+1)



def quickSort(arr,inicio,final):
	if inicio<final:
		part = dividir(arr,inicio,final)
		
		quickSort(arr,inicio,part-1)
		quickSort(arr,part+1,final)



n = int(input())
print(n)

arr = [0]*n

for i in range(n):
	arr[i] = random.randint(0,n)

print('Arreglo sin ordenar: ')
print(arr)
quickSort(arr,0,n-1)
print('Arreglo ordenado por Quicksort: ')
print(arr)
