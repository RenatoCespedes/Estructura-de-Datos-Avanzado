#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;
void crear(int *&A,int n)
{
	A=new int[n];
}
void max_heap(int arr[],int n, int i)
{
	int mayor = i;
	int l = 2*i + 1;
	int r = 2*i + 2;
	if (l < n && arr[l] > arr[mayor])
		mayor = l;
	if (r < n && arr[r] > arr[mayor])
		mayor = r;
	if (mayor != i)
	{
		swap(arr[i], arr[mayor]);
		max_heap(arr, n, mayor);
	}
}
void heapSort(int arr[],int n)
{
	for (int i = n / 2 - 1; i >= 0; i--)
		max_heap(arr, n, i);
	for (int i=n-1; i>0; i--)
	{
		swap(arr[0], arr[i]);
		max_heap(arr, i, 0);
	}
}
void printArray(int arr[], int n)
{
	for (int i=0; i<n; ++i)
		cout << arr[i] << " ";
	cout << "\n";
}
int main()
{
    int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Heap.txt");
	srand(time(NULL));
	for(int i=n;i<=600000;i=i+60000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		heapSort(A,i);
		t0=clock()-t0;
		time1=((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}

}
