#include <iostream>
using namespace std;
void BubbleSort(int* arr, int tam){
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
void printi(int *arr,int tam){
    for(int i=0;i<tam;i++){
        cout<<arr[i]<<' ';
    }
    cout<<endl;
}
int main(){
    int a[3] = {9,5,1};
    printi(a,3);
    BubbleSort(a,3);
    printi(a,3);
    return 0;
}
