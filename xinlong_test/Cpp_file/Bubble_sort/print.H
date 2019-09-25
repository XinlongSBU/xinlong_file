#include <iostream>
using namespace std;

// LIMITATION: iostream , iomanip
// It prints the array's contents in rows of 20.
void PrintArray (int ArrayName[] , const int ArraySize)
{
	cout << setiosflags(ios::left);
	for (int i = 0 ; i < ArraySize ; i++)
	{
		cout << setw(3) << ArrayName[i];
		if (i+1 % 20 == 0)
			cout << endl;
	}
	cout << endl;
}
