
public class HeapSort 
{ 
	public void sort(int arr[]) 
	{ 
		int n = arr.length; 
		for (int i = n / 2 - 1; i >= 0; i--) 
			maxheap(arr, n, i); 

		for (int i=n-1; i>0; i--) 
		{ 
			int temp = arr[0]; 
			arr[0] = arr[i]; 
			arr[i] = temp; 
			maxheap(arr, i, 0); 
		} 
	} 
	void maxheap(int arr[], int n, int i) 
	{ 
		int largest = i; 
		int l = 2*i + 1; 
		int r = 2*i + 2; 
		if (l < n && arr[l] > arr[largest]) 
			largest = l; 
		if (r < n && arr[r] > arr[largest]) 
			largest = r; 
		if (largest != i) 
		{ 
			int swap = arr[i]; 
			arr[i] = arr[largest]; 
			arr[largest] = swap; 
			maxheap(arr, n, largest); 
		} 
	} 
	static void printArray(int arr[]) 
	{ 
		int n = arr.length; 
		for (int i=0; i<n; ++i) 
			System.out.print(arr[i]+" "); 
		System.out.println(); 
	} 
	public static void main(String args[]) 
	{ 
		int arr[] = {51,13,2,45,9,89,65,12,13}; 
		int n = arr.length; 

		HeapSort ob = new HeapSort(); 
		ob.sort(arr); 

		System.out.println("Lista ordenada :"); 
		printArray(arr); 
	} 
} 
