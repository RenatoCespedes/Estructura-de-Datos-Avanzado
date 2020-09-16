#include <bits/stdc++.h> 
using namespace std; 


void swap(int* a, int* b) 
{ 
	int t = *a; 
	*a = *b; 
	*b = t; 
} 


int partition (int arr[], int inic, int high) 
{ 
	int pivot = arr[high]; 
	int i = (inic - 1);  

	for (int j = inic; j <= high - 1; j++) 
	{ 
		
		if (arr[j] < pivot) 
		{ 
			i++;  
			swap(&arr[i], &arr[j]); 
		} 
	} 
	swap(&arr[i + 1], &arr[high]); 
	return (i + 1); 
} 

void quickSort(int arr[], int inicio, int fin) 
{ 
	if (inicio < fin) 
	{ 
		
		int pi = partition(arr, inicio, fin); 

		// Separately sort elements before 
		// partition and after partition 
		quickSort(arr, inicio, pi - 1); 
		quickSort(arr, pi + 1, fin); 
	} 
} 

int main()
{
	
}
