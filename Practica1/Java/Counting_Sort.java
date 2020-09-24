import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Counting_Sort {
    public static void main(String[] args) throws IOException,FileNotFoundException {
        File file=new File("TiemposJava/CountingSortJ.txt");
        
        
        long time1, time2;
        
        FileWriter fw = new FileWriter(file);
        BufferedWriter bw = new BufferedWriter(fw);
        for(int i=10000;i<=100000;i=i+10000)
        {
          int[] a=new int[i];
          // System.out.println(" indice"+ ( id ));
          leer(a,i);
          int k=max(a);
          time1=System.currentTimeMillis();
          // time1=System.currentTimeMillis();
          countSort(a,k);
          time2=System.currentTimeMillis();
          long tiempo=time2-time1;
          // time2=System.currentTimeMillis();

          System.out.println("Tiempo "+ ( tiempo ) +" s");
          String s=String.valueOf(tiempo);
          
          
            
            bw.write(s+'\n');
           
          
        }
         bw.close();
               
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

    public static int max(int[] array) {
    if (array.length == 0) {
        // ...
    }

    int max = array[0];

    for (int a : array) {
        if (a > max)
            max = a;
    }

    return max;
}
    public static void countSort(int[] array,int tam)
	{
	    
		int[] contador=new int[tam+1];

		for(int i:array){
			contador[i]++;
		}

		int x=0;
		for(int i=0;i<contador.length;i++)
		{
			while(0<contador[i]){
				array[x++]=i;
				contador[i]--;
			}
		}
	}
}



   



