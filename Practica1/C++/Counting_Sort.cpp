#include <bits/stdc++.h>
#include "../GeneradorAleatorio/generator.h"
using namespace std;




void crear(int *&A,int n)
{
	A=new int[n];
}
void llenar(int *A,int n)
{
	for(int i=0;i<n;i++)
	{
		*(A+i)= rand()%1000;
	}
}
void imprimir(int *A,int n)
{
	for(int i=0;i<n;i++)
	{
		cout<<A[i]<<" ";
	}
	cout<<endl;
}
/////////////////////COUNTING SORT////////////////////////////
void countingSort(int *A,int tam)
{
	int max=*(A);
	int min=*(A);

	for(int i=0;i<tam;i++)
	{
		max=(*(A+i)>max)?*(A+i):max;
		min=(*(A+i)<min)? *(A+i):min;
	}

	int range=max - min +1;
	int *B=new int[range];

	for(int j=0;j<range;j++)
	{
		*(B+j)=0;
	}

	for(int i=0;i<tam;i++){
		B[A[i]-min]++;
//		*(B+(*(A+i)-min))++;
	}
	int p=0;
	for(int i=min;i<=max;i++)
	{
		for(int j=0;j<*(B+(i-min));j++)
		{
			*(A+(p++))=i;
		}
	}


}

int main()
{
	int n=10000;
	double t0;
	double time1;
	int k=0;
	ofstream fs("Tiempos/time_Counting.txt");
	srand(time(NULL));
	for(int i=n;i<=600000;i=i+60000){
		int *A;
		crear(A,i);
		read(A,i,k);
		t0=clock();
		countingSort(A,i);
		t0=clock()-t0;
		time1= ((double)t0)/CLOCKS_PER_SEC;
		k++;
		fs<<time1<<endl;
	}

	return 0;
}
