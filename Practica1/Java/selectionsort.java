import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class selectionsort {
	public static void swap(int minimo,int i){
		int temp=minimo;
		minimo=i;
		i=temp;
	}
	public static void selectionsort(int[] A){
		int tam= A.length;
		for(int i=0;i<tam-1;i++){
			int minimo=i;
			for(int j=i+1;j<tam;j++){
				if(A[j]<A[minimo]){
					minimo=j;
				}
			}
			int temp=A[minimo];
			A[minimo]=A[i];
			A[i]=temp;
		}
	}
	public static void print(int[] A){
		for(int i:A){
			System.out.print(i+" ");
		}
	}public static void leer(int[] a,int tam) throws FileNotFoundException,IOException{
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
	
	public static void main(String args[]) throws FileNotFoundException,IOException
	{
		File file=new File("TiemposJava/Selection_Sort.txt");
        long time1, time2;
        FileWriter fw = new FileWriter(file);
		BufferedWriter bw = new BufferedWriter(fw);
		for(int i=10000;i<=100000;i=i+10000)
        {
          int[] a=new int[i];
          // System.out.println(" indice"+ ( id ));
          leer(a,i);
          selectionsort select = new selectionsort();
          time1=System.currentTimeMillis();
          // time1=System.currentTimeMillis();
          select.selectionsort(a);
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