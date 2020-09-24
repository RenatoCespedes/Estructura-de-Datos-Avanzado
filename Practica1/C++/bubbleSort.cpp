#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;
void crear(int *&A,int n)
{
	A=new int[n];
}
void BubbleSort(int *arr, int tam){
    for(int i=0;i<tam;i++){
        for(int j=0;j<tam;j++){
            if(arr[j]>arr[i]){
                int aux = arr[j];
                arr[j] = arr[i];
                arr[i] = aux;
            }
        }
    }
}
int main(){
	int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Bubble.txt");
	srand(time(NULL));
	for(int i=n;i<=600000;i=i+60000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		BubbleSort(A,i);
		t0=clock()-t0;
		time1= ((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}
    return 0;
}
