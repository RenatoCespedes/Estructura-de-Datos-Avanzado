class InsertionSort{
    void insertionSort(int arr[]) { 
        int n = arr.length; 
        for (int i = 1; i < n; ++i) { 
            int key = arr[i]; 
            int j = i - 1;
            while (j >= 0 && arr[j] > key) { 
                arr[j + 1] = arr[j]; 
                j = j - 1; 
            } 
            arr[j + 1] = key; 
        }
    }
    void printi(int arr[]){
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    }
}
public class Main{
    public static void main(String args[]) {
        int arr[] = {64, 34, 25, 12, 22, 11, 90};
        InsertionSort ob = new InsertionSort(); 
        ob.insertionSort(arr); 
        ob.printi(arr); 
    }
}
