 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

void pretty_printer(int *to_print);


int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 2)
    {
        printf("Usage: ./selsort [asc|dsc]\n");
        return 1;
    }
    
    // TODO asc, dsc

    //helpers
    int limit = sizeof(to_sort)/sizeof(to_sort[0]);
    int max;
    int maxIndex;
    //why this way? :)
    for (int i = limit - 1; i > 0; i--)
    {
        //TODO
    }

    pretty_printer(to_sort);
    return 0;
}

void pretty_printer(int *to_print)
{
    printf("[");
    for (int i = 0, j = sizeof(to_sort)/sizeof(to_sort[0]); i < j; i++)
    { 
        if (i == j - 1)
        {
            printf("%i", to_print[i]);
            break;
        }
        printf("%i, ", to_print[i]);
    }
    printf("]\n");
}
