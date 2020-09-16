#include <iostream>

using namespace std;

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
    int a[3] = {9,5,1};
    printi(a,3);
    insertionSort(a,3);
    printi(a,3);
    return 0;
}