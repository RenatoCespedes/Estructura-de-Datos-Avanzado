import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

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
    public static void main(String[] args) throws FileNotFoundException,IOException{

        File file=new File("TiemposJava/quicksort.txt");
        
        long time1, time2;
        FileWriter fw = new FileWriter(file);
        BufferedWriter bw = new BufferedWriter(fw);
        for(int i=10000;i<=100000;i=i+10000)
        {
          int[] a=new int[i];
          // System.out.println(" indice"+ ( id ));
          leer(a,i);
          quicksort quick = new quicksort();
          time1=System.currentTimeMillis();
          // time1=System.currentTimeMillis();
          quick.qsort(a,0,a.length-1);
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
