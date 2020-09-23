#from time import time
def selectionsort(A):
	tam=len(A)
	for i in range(tam):
		minimo =i
		for j in range(i+1,tam):
			if A[j]<A[minimo]:
				minimo=j
		tempo=A[i]
		A[i]=A[minimo]
		A[minimo]=tempo

print("Selection Loaded")
"""A=[15,3,6,9,3,5,12,4,0,48,42]
start_time=time()
selectionsort(A)
elapsed_time=time()-start_time
print("Tiempo: %0.10f seconds." % elapsed_time)
print(A)"""
