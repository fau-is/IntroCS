#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>


int main(int argc, char **argv)
{
    if(argc != 2)
    {
        printf("Please only enter the number you would like the square root for\n");
        return 1;
    }

    float x = 1, no = atof(argv[1]), root1 = (x +(no/x))/2;

    while (true)
    {
        float root2 = (root1 + (no/root1))/2;
        //printf("1\n");

        if (root2 == root1)
        {
            printf("The Square root of %s = %.5f\n", argv[1], root2);
            return 0;
        }

        root1 = root2;
    }
}