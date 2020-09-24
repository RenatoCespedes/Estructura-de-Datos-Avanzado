#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;
void crear(int *&A,int n)
{
	A=new int[n];
}
void insertionSort(int *arr, int size) {
   int key, j;
   for(int i = 1; i<size; i++) {
      key = arr[i];
      j = i;
      while(j > 0 && arr[j-1]>key) {
         arr[j] = arr[j-1];
         j--;
      }
      arr[j] = key;
   }
}

void printi(int *arr,int tam){
    for(int i=0;i<tam;i++){
        cout<<arr[i]<<' ';
    }
    cout<<endl;
}

int main(){
	int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Insertion.txt");
	srand(time(NULL));
	for(int i=n;i<=600000;i=i+60000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		insertionSort(A,i);
		t0=clock()-t0;
		time1= ((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}

}
