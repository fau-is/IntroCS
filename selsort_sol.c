 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

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

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 2)
    {
        printf("Usage: ./selsort [asc|dsc]\n");
        return 1;
    }
    if (strcmp(argv[1], "asc") == 0)
    {
        asc = 1;
    }
    else if (strcmp(argv[1], "dsc") == 0)
    {
        asc = 0;
    }
    else
    {
        printf("Usage: ./selsort [asc|dsc]\n");
        return 1;
    }

    //helpers
    int limit = sizeof(to_sort)/sizeof(to_sort[0]);
    int max;
    int maxIndex;
    //why this way? :)
    for (int i = limit - 1; i > 0; i--)
    {
        max = to_sort[i];
        maxIndex = i;
        for (int j = 0; j < i; j++)
        {
            bool cond = to_sort[j] >= max;
            if (!asc)
            {
                cond = !cond;
            }
            if (cond)
            {
                max = to_sort[j];
                maxIndex = j;
            }
        }
        int tmp = to_sort[i];
        to_sort[i] = to_sort[maxIndex];
        to_sort[maxIndex] = tmp;
    }

    pretty_printer(to_sort);
    return 0;
}
