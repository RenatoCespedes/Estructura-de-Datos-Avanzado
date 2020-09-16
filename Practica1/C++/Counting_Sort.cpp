#include <iostream>
#include <fstream>
#include<stdlib.h>
#include<time.h>

using namespace std;





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
	
	for(int j=0;j<tam;j++)
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
	int n;
	cout<<"Ingrese el size del array: ";
	cin>>n;
	int *A=new int[n];
	int *B=new int[n];
	srand(time(NULL));
	for(int i=0;i<n;i++)
	{
		*(A+i)= rand()%n;
//		*(B+i)=*(A+i);
	}
	float t0=clock();
	cout<<"Array"<<endl;
	imprimir(A,n);

	
	cout<<"Counting"<<endl;
	countingSort(A,n);
	imprimir(A,n);
	

	return 0;
}
