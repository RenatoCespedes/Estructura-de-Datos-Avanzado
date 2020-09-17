import java.util.Scanner;




public class mergesort{

    void merge(int arr[],int izq,int m,int der){
        int n1 = m-izq+1;
        int n2 = der-m;

        int L[] = new int[n1]; 
        int R[] = new int[n2];

        for(int i=0;i<n1;i++){
            L[i] = arr[izq+i];
        }
        for(int i=0;i<n2;i++){
            R[i] = arr[m+1+i];
        }

        int i=0;
        int j=0;
        int x= izq;

        while(i<n1 && j<n2){
            if (L[i] <= R[j]){ 
                arr[x] = L[i]; 
                i++; 
            }
            else { 
                arr[x] = R[j]; 
                j++; 
            } 
            x++;
            
        }
        while (i < n1) { 
            arr[x] = L[i]; 
            i++; 
            x++; 
        } 
        while (j < n2) { 
            arr[x] = R[j]; 
            j++; 
            x++; 
        } 
    }


    void msort(int arr[],int izq, int der){
        if(izq<der){
            int m = (izq+der)/2;

            msort(arr,izq,m);
            msort(arr,m+1,der);

            merge(arr,izq,m,der);
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
        mergesort merge = new mergesort(); 
        merge.msort(arr,0,n-1);
        print(arr); 
    }
}