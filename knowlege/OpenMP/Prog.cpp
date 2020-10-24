#include<iostream>
using namespace std;

int pro(){
    double x;
    double A[100], B[100], C[100];
    int i;

    #pragma omp parallel for private (i,x)

    for (i=0; i<100; i++){
        x = A[i] + B[i];
        C[i] = x + 1/x;

    }
    cout<<"x ="<<x<<endl;
    return 0   ;
}

 
