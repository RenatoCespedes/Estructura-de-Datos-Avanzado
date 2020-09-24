import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class heapsort
{ 
	public void sort(int arr[]) 
	{ 
		int n = arr.length; 
		for (int i = n / 2 - 1; i >= 0; i--) 
			maxheap(arr, n, i); 

		for (int i=n-1; i>0; i--) 
		{ 
			int temp = arr[0]; 
			arr[0] = arr[i]; 
			arr[i] = temp; 
			maxheap(arr, i, 0); 
		} 
	} 
	void maxheap(int arr[], int n, int i) 
	{ 
		int largest = i; 
		int l = 2*i + 1; 
		int r = 2*i + 2; 
		if (l < n && arr[l] > arr[largest]) 
			largest = l; 
		if (r < n && arr[r] > arr[largest]) 
			largest = r; 
		if (largest != i) 
		{ 
			int swap = arr[i]; 
			arr[i] = arr[largest]; 
			arr[largest] = swap; 
			maxheap(arr, n, largest); 
		} 
	} 
	static void printArray(int arr[]) 
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
	
	public static void main(String args[]) throws FileNotFoundException,IOException
	{
		File file=new File("TiemposJava/heapsort.txt");
        long time1, time2;
        FileWriter fw = new FileWriter(file);
		BufferedWriter bw = new BufferedWriter(fw);
		for(int i=10000;i<=100000;i=i+10000)
        {
          int[] a=new int[i];
          // System.out.println(" indice"+ ( id ));
          leer(a,i);
          heapsort heap = new heapsort();
          time1=System.currentTimeMillis();
          // time1=System.currentTimeMillis();
          heap.sort(a);
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
