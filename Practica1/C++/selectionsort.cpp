#include<iostream>
#include <time.h>
using namespace std;

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
    unsigned t0,t1;
    srand(time(NULL));

    int arr[] = {64,10,1,9,85,36,14,3,6, 25, 12, 22, 11};  
    int n = sizeof(arr)/sizeof(arr[0]);
    t0=clock();
    selectionSort(arr, n); 
    t1=clock();
    print(arr, n);  
    double time=(double(t1-t0)/CLOCKS_PER_SEC);
    cout<<"Tiempo 1 "<<time<<endl;
    return 0;  
} 