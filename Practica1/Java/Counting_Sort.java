import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Your code here!
        
        int[] a={60, 40, 30, 20, 10, 40, 30, 60, 60, 20, 40, 30, 40};
		int k=60;

		System.out.println("Array Generado");
		System.out.println(Arrays.toString(a));

		countSort(a,k);
		System.out.println("countSort");
		System.out.println(Arrays.toString(a));
        
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



   



