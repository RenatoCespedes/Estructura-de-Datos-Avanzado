#include <iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;

void Aleatorio(unsigned long int& n,unsigned long int* arreglo){
    srand(time(nullptr));
    unsigned long int num;
    for (unsigned long int i =0;i<n;i++){
        num = 1+rand()%n;
        arreglo[i] = num;
    }
    cout<<endl;
    
}

void merge(unsigned long int arr[],unsigned long int izq,unsigned long int m,unsigned long int der) 
{ 
    unsigned long int i, j, k; 
    unsigned long int n1 = m - izq + 1; 
    unsigned long int n2 =  der - m; 
  
    unsigned long int* L;
    unsigned long int* R; 
    L = new unsigned long[n1];
    R = new unsigned long[n2];
   
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
void mergeSort(unsigned long int arr[], unsigned long int izq, unsigned long int der) 
{ 
    if (izq < der) 
    { 
        unsigned long m = izq+(der-izq)/2; 
  
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
    unsigned long int n;
    unsigned t1,t2;
    unsigned long int *arreglo = nullptr;
    cout<<"Que tamanio de arreglo quieres"<<endl;
    cin>>n;
    arreglo = new unsigned long int[n];
    Aleatorio(n,arreglo);
    //cout<<"Desordenado"<<endl;
    //print(n,arreglo);
    t1=clock();
    mergeSort(arreglo,0,n-1);
    t2=clock();
    double time = (double(t2-t1)/CLOCKS_PER_SEC);
    cout<<time*1000<<endl;
    delete[] arreglo;
    return 0;
}