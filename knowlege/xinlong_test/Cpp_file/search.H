#include <iostream>
using namespace std;

void search(int Array1[], int length, int a)
{
	int f = 0;
	for(int i=0; i<length; i++)
	{
		if(Array[i] == a){
			cout<<"Found! Index is "<<i<<" !"<<endl;
			f = 1;
		}
		
	}
	if(f == 0)
	{
		cout<<"Not Found!"<<endl;
	}	
}

