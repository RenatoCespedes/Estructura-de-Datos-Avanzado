#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;
void crear(int *&A,int n)
{
	A=new int[n];
}
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n)
{
    int minimo;
    for (int i = 0; i < n-1; i++){
        minimo = i;
        for (int j = i+1; j < n; j++){
        	if (arr[j] < arr[minimo])
            	minimo = j;
  }
        	swap(&arr[minimo], &arr[i]);


    }
}

void print(int arr[], int tam)
{
    int i;
    for (i=0; i < tam; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Selection.txt");
	srand(time(NULL));
	for(int i=n;i<=600000;i=i+60000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		selectionSort(A,i);
		t0=clock()-t0;
		time1= ((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}
    return 0;
}
