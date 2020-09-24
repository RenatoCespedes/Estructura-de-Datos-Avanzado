#include <bits/stdc++.h>
#include "generator.h"
using namespace std;





 int main(){
 	int n=10000,k=0;
 	ofstream fs("Tama.txt");
 	for(int i=n;i<600000;i+=60000){
 		GenerarArray(i,k);
 		fs<<i<<" ";
 		k=k+1;
 		
	 }
 }
