import java.util.*;
public class quicksort {
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
    int divrandom(int arr[],int inicio,int fin){
        Random rand = new Random();
        int pivot = rand.nextInt(fin-inicio)+inicio;
        int swap = arr[pivot];
        arr[pivot] = arr[fin];
        arr[fin] = swap;
        return dividir(arr,inicio,fin);
    }
    void qsort(int arr[],int inicio,int fin){
        if(inicio<fin){
            int part = divrandom(arr,inicio,fin);
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
        long t1, t2, tt;
        Scanner entrada = new Scanner(System.in);
        n = entrada.nextInt();
        int[] arr = new int[n];
        generar(arr,n);
        //System.out.println("Arreglo Desordenado");
        quicksort quick = new quickal(); 
        t1=System.currentTimeMillis();
        quick.qsort(arr,0,n-1);
        t2= System.currentTimeMillis();
        tt=t2-t1;
        System.out.println("Tiempo de ejecucion: "+tt);
        //print(arr); 
    }
}
