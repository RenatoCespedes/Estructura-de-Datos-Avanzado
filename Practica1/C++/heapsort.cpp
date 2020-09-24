// C++ program for implementation of Heap Sort
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
void max_heap(long long arr[], long long n, int i)
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
void heapSort(long long arr[], long long n)
{
	for (int i = n / 2 - 1; i >= 0; i--)
		max_heap(arr, n, i);
	for (int i=n-1; i>0; i--)
	{
		swap(arr[0], arr[i]);
		max_heap(arr, i, 0);
	}
}
void printArray(long long arr[], long long n)
{
	for (int i=0; i<n; ++i)
		cout << arr[i] << " ";
	cout << "\n";
}
int main()
{
    ofstream archivo("time.txt");

	long long arr[100000];
	srand(time(NULL));
	long long  num;
	float t0;
	double time1;
	for(long long i=0;i<100000;i++)
    {
        num=1+rand()%(10000-1);
        arr[i]=num;
    }
	long long n = sizeof(arr)/sizeof(arr[0]);
    cout << "lista desordenada"<<endl;
    t0=clock();
	heapSort(arr, n);
	t0=clock()-t0;
	time1= ((double)t0)/CLOCKS_PER_SEC;
    printf (" m_Sec :%d (%f seconds).\n",t,((float)t)/CLOCKS_PER_SEC);
    archivo<<t<<endl;
	/*cout << "lista construida y ordenada: " <<endl;
	printArray(arr, n);*/
}
