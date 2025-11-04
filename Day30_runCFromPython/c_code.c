#include<stdio.h>
int main(int numOfArguments, int *args[])
{   int i=0;
    printf("Argument count: %d\n",numOfArguments);
    for ( i; i <numOfArguments; i++)
    {
        if (i==0)
            continue;
        printf("%d) %s\n",i,args[i]);
    }
    
    return 0;
}