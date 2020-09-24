#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;
void crear(int *&A,int n)
{
	A=new int[n];
}
void Aleatorio(unsigned long int& n,unsigned long int* arreglo){
    srand(time(nullptr));
    unsigned long int num;
    for (unsigned long int i =0;i<n;i++){
        num = 1+rand()%n;
        arreglo[i] = num;
    }
    cout<<endl;

}

void merge(int arr[], int izq,int m, int der)
{
    int i, j, k;
    int n1 = m - izq + 1;
    int n2 =  der - m;

    int* L;
    int* R;
    L = new int[n1];
    R = new int[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[izq + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];


    i = 0;
    j = 0;
    k = izq;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
    delete[] L;
    delete[] R;
}
void mergeSort(int arr[], int izq, int der)
{
    if (izq < der)
    {
        int m = izq+(der-izq)/2;

        mergeSort(arr, izq, m);
        mergeSort(arr, m+1, der);

        merge(arr, izq, m, der);
    }
}
void print(int& n, int* arreglo){
    for(int i=0;i<n;i++){
        cout<<arreglo[i]<<" ";
    }
    cout<<endl;
}
int main(){
    int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Merge.txt");
	srand(time(NULL));
	for(int i=n;i<=600000;i=i+60000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		mergeSort(A,0,n-1);
		t0=clock()-t0;
		time1= ((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}

    return 0;
}
