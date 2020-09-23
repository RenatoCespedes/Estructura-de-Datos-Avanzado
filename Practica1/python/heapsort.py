
def max_heap(arr, n, i): 
	largest = i 
	l = 2 * i + 1	
	r = 2 * i + 2	 
	if l < n and arr[i] < arr[l]: 
		largest = l 
	if r < n and arr[largest] < arr[r]: 
		largest = r 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] 
		max_heap(arr, n, largest) 
def heapSort(arr): 
	n = len(arr) 
	for i in range(n//2 - 1, -1, -1): 
		max_heap(arr, n, i) 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		max_heap(arr, i, 0) 

print("Heap Loaded")
"""arr = [51,13,2,45,9,89,65,12,13] 
heapSort(arr) 
n = len(arr) 
print ("Lista ordenada :") 
for i in range(n): 
	print ("%d" %arr[i]), """
