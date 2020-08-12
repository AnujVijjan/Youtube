#include<iostream>

using namespace std;

// Global varable declaration
// int g;
int g = 30;

int main()
{
    // Local varable declaration
    int a;
    
    cout<<"G="<<g; 
    //Variable initialization
    a = 10;
    g = 20;


    cout<<"A="<<a;   
    cout<<"G="<<g;   
    return 0;
}



// Initializing Local and Global Variables

/* Data Type	Initializer
int	                  0
char	            '\0'
float	              0
double	              0
pointer         	NULL */
