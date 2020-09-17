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


A=[15,3,6,9,3,5,12,4,0,48,42]
selectionsort(A)
print(A)