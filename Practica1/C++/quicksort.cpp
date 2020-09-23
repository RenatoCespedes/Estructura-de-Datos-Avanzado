#include <iostream>
#include<stdlib.h>
#include<time.h>
#include <cstdlib> 
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
    int n;
    unsigned t1,t2;
     int *arreglo = nullptr;
    cout<<"Que tamanio de arreglo quieres"<<endl;
    cin>>n;
    arreglo = new int[n];
    Aleatorio(n,arreglo);
    t1 = clock();
    quickSort(arreglo,0,n-1);
    t2 = clock();
    double time = (double(t2-t1)/CLOCKS_PER_SEC);
    cout<<time*1000<<endl;
    //print(n,arreglo);
    delete[] arreglo;
    return 0;
}
