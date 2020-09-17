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

void print(int& n, int* arreglo){
    for(int i=0;i<n;i++){
        cout<<arreglo[i]<<" ";
    }
    cout<<endl;
}

void swap(int* a, int* b)  
    {  
        int t = *a;  
        *a = *b;  
        *b = t;  
    }
int dividir( int arr[],int inicio, int final){
    int pivot = arr[final];
    int x = (inicio-1);
    for (int i = inicio; i <= final-1; i++)
    {
        if (arr[i] < pivot)
        {
            x++;
            swap(&arr[x],&arr[i]);
        }
        
    }
    swap(&arr[x+1],&arr[final]);
    
    return (x+1);
    
}

void quickSort(int arr[],int inicio, int final){
    if (inicio<final)
    {
        int part = dividir(arr,inicio,final);

        quickSort(arr,inicio,part-1);
        quickSort(arr,part+1,final);
    }
    
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
    quickSort(arreglo,0,n-1);
    cout<<"Ordenado usando QuickSort"<<endl;
    
    print(n,arreglo);
    delete[] arreglo;
    return 0;
}