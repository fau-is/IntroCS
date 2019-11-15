#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

// Helper to print arrays
void pretty_printer(int *to_print, int size);

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 2)
    {
        printf("Usage: ./selsort [asc|dsc]\n");
        return 1;
    }
   

    //TODO: check if sorting in asc (ascending) or dsc (descending) order


    //helpers
    int limit = sizeof(to_sort)/sizeof(to_sort[0]);
    int max;
    int maxIndex;
    //TODO implement Selection Sort
    // HINT: We are reducing the limit from the right side on
    for (int i = limit - 1; i > 0; i--)
    {


        //TODO

    }
    pretty_printer(to_sort, 10)
    return 0;
}

void pretty_printer(int *to_print, size_t size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        if (i == size - 1)
        {
            printf("%i", to_print[i])   
        }
        else
        {
            printf("%i, ", to_print[i]);
        }
    }
    printf("]\n");
}
