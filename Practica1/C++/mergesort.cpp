#include <iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;

void Aleatorio(int& n,int* arreglo){
    srand(time(nullptr));
    int num;
    for (int i =0;i<n;i++){
        num = 1+rand()%n;
        arreglo[i] = num;
    }
    cout<<endl;
    
}

void merge(int arr[], int izq, int m, int der) 
{ 
    int i, j, k; 
    int n1 = m - izq + 1; 
    int n2 =  der - m; 
  
    int L[n1], R[n2]; 
  
   
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
    int n;
    int *arreglo = nullptr;
    cout<<"Que tamanio de arreglo quieres"<<endl;
    cin>>n;
    arreglo = new int[n];
    Aleatorio(n,arreglo);
    cout<<"Desordenado"<<endl;
    print(n,arreglo);
    mergeSort(arreglo,0,n-1);
    cout<<"Ordenado usando MergeSort"<<endl;
    print(n,arreglo);
    delete[] arreglo;
    return 0;
}