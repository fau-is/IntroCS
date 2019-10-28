#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if (argc != 3)
 	{
        printf("Usage: ./babylon k a\n");
        return 1;
    }
    int k = atoi(argv[1]);
    int a = atoi(argv[2]);
    float eps = 0.01;

    //TODO: conditions where execution is rejected. Make sure "Try again...\n" is printed!

    //TODO: follow instructions
    
    //TODO: print result with 5 decimal places
    return 0;
}