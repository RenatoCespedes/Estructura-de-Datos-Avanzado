import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

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

    public static void leer(int[] a,int tam) throws FileNotFoundException,IOException{
        int numeroEntero,indice=0;
        File f=new File("../GeneradorAleatorio/Array_"+tam+".txt");
        try(Scanner entrada = new Scanner(f)){
          while (entrada.hasNextInt() && indice<tam) { 
                numeroEntero = entrada.nextInt();
                a[indice]=numeroEntero;
                indice++;
            }
        }catch (FileNotFoundException e) {
        }
    }


    public static void main(String[] args) throws FileNotFoundException,IOException {
        /*
        int n = 0;
        Scanner entrada = new Scanner(System.in);
        n = entrada.nextInt();
        int[] arr = new int[n];
        long t1,t2,tt;
        generar(arr,n);
        System.out.println("Arreglo Desordenado");
        print(arr); 
        System.out.println("Arreglo Desordenado");
        mergesort merge = new mergesort();
        t1 = System.currentTimeMillis();  
        merge.msort(arr,0,n-1);
        t2 = System.currentTimeMillis();
        tt = t2-t1;
        System.out.println(tt);
        */

        File file=new File("TiemposJava/mergesort.txt");
        
        
        long time1, time2;
        FileWriter fw = new FileWriter(file);
        BufferedWriter bw = new BufferedWriter(fw);
        for(int i=10000;i<=100000;i=i+10000)
        {
          int[] a=new int[i];
          // System.out.println(" indice"+ ( id ));
          leer(a,i);
          mergesort merge = new mergesort();
          time1=System.currentTimeMillis();
          // time1=System.currentTimeMillis();
          merge.msort(a,0,a.length-1);
          time2=System.currentTimeMillis();
          long tiempo=time2-time1;
          // time2=System.currentTimeMillis();

          System.out.println("Tiempo "+ ( tiempo ) +" s");
          String s=String.valueOf(tiempo);
          
            
            bw.write(s+'\n');
        }
        bw.close();
    }
}