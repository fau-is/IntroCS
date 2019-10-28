#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

void pretty_printer(int *to_print, int size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        printf("%i, ", to_print[i]);
    }
    printf("]\n");
}

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 2)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }
   

    //same as in bubble sort


    //helpers
    int limit = sizeof(to_sort)/sizeof(to_sort[0]);
    int max;
    int maxIndex;
    //why this way? :)
    for (int i = limit - 1; i > 0; i--)
    {


        //TODO

    }


    //TODO


    return 0;
}