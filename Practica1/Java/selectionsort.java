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
	}
	public static void main(String[] args) {
		int [] A={15,2,6,9,8,5,14,3,0,56,4,1};
		selectionsort(A);
		print(A);
	}

}