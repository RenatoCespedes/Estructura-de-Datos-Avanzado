import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class bubbleSort{

    void bubble(int arr[]) { 
        int n = arr.length; 
        for (int i = 0; i < n-1; i++) 
            for (int j = 0; j < n-i-1; j++) 
                if (arr[j] > arr[j+1]){
                    int temp = arr[j]; 
                    arr[j] = arr[j+1]; 
                    arr[j+1] = temp; 
                } 
    } 

    void printi(int arr[]){
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 

    public static void leer(int[] a,int tam) throws FileNotFoundException,IOException{
        int numeroEntero,indice=0;
        File f=new File("../GeneradorAleatorio/GeneratedArray"+tam+".txt");
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

        File file=new File("TiemposJava/bubblesort.txt");
        long time1, time2;
        FileWriter fw = new FileWriter(file);
        BufferedWriter bw = new BufferedWriter(fw);
        for (int i = 10000; i <=100000; i=i+10000) {
            int[] a=new int[i];
          // System.out.println(" indice"+ ( id ));
            leer(a,i);
            bubbleSort bub = new bubbleSort();
            time1=System.currentTimeMillis();
             // time1=System.currentTimeMillis();
            bub.bubble(a);
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
