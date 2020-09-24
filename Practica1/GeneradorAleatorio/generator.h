#ifndef GENERADOR_H
#define GENERADOR_H

#include<bits/stdc++.h>

using namespace std;

int Generar(int n,int k){
	srand(time(NULL));
//	cout<<k<<endl;
	ofstream fs("GeneratedMatrix"+std::to_string(k)+".txt");
	k++;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++){
			fs<<rand()%(n*100)<<" ";
		}
		fs<<endl;
	}
	fs.close();
	return k;
}

void leer(int **A,int n,int k){
	ifstream fe("GeneratedMatrix"+std::to_string(k)+".txt");
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			fe>>*(*(A+i)+j);
		}
	}
	fe.close();
}

void GenerarArray(int n,int k)
{
	srand(time(NULL));
	ofstream fs("GeneratedArray"+std::to_string(k)+".txt");

	for(int j=0;j<n;j++){
		fs<<rand()%(n*100)<<" ";
	}
	fs.close();

}

void read(int *A,int n,int k){
	ifstream fe("../GeneradorAleatorio/GeneratedArray"+std::to_string(k)+".txt");
	for(int i=0;i<n;i++){
		fe>>*(A+i);
	}
	fe.close();
}


#endif //GENERADOR_H
