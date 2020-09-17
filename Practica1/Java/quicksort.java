import java.util.Scanner;




public class quicksort{



    int dividir(int arr[],int inicio,int fin){
        int pivot = arr[fin];
        int x= inicio-1;
        for(int i=inicio;i<fin;i++ ){
            if(arr[i]< pivot){
                x++;
                int swap = arr[x];
                arr[x] = arr[i];
                arr[i] = swap; 
            }
        }
        int swap = arr[x+1];
        arr[x+1] = arr[fin];
        arr[fin] = swap;
        return x+1; 
    }
    void qsort(int arr[],int inicio,int fin){
        if(inicio<fin){
            int part = dividir(arr,inicio,fin);
            qsort(arr,inicio,part-1);
            qsort(arr,part+1,fin);
        }
    }
    
    static void print(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 

    static void generar(int arr[],int n){
        int rand = 0;
        for(int i=0;i<n;i++){
            rand=(int)(Math.random()*n+1);
            arr[i] = rand;
        }

    }


    public static void main(String[] args) {
        int n = 0;
        
        Scanner entrada = new Scanner(System.in);
        n = entrada.nextInt();
        int[] arr = new int[n];
        generar(arr,n);
        System.out.println("Arreglo Desordenado");
        print(arr); 
        System.out.println("Arreglo Desordenado");
        quicksort quick = new quicksort(); 
        quick.qsort(arr,0,n-1);
        print(arr); 
    }
}