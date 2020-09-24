#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;
void crear(int *&A,int n)
{
	A=new int[n];
}
void Aleatorio(int& n,int* arreglo){
    srand(time(nullptr));
    int num;
    for (int i =0;i<n;i++){
        num = 1+rand()%n;
        arreglo[i] = num;
    }
    cout<<endl;

}

void print(int& n, int* arreglo){
    for(int i=0;i<n;i++){
        cout<<arreglo[i]<<" ";
    }
    cout<<endl;
}

int dividir(int arr[], int inicio, int fin)
{
    int pivot = arr[fin];
    int i = (inicio - 1);

    for (int j = inicio; j <= fin - 1; j++) {

        if (arr[j] <= pivot) {

            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[fin]);
    return (i + 1);
}

int divrandom(int arr[], int low, int high)
{
    srand(time(NULL));
    int random = low + rand() % (high - low);

    swap(arr[random], arr[high]);

    return dividir(arr, low, high);
}

void quickSort(int arr[], int inicio, int fin)
{
    if (inicio < fin) {


        int pi = divrandom(arr, inicio, fin);

        quickSort(arr, inicio, pi - 1);
        quickSort(arr, pi + 1, fin);
    }
}

int main(int argc, char const *argv[])
{
    int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Quick.txt");
	srand(time(NULL));
	for(int i=n;i<=100000;i=i+10000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		quickSort(A,0,i-1);
		t0=clock()-t0;
		time1= ((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}
    return 0;
}