#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char *to_sort = "zdvixqcuvd";
//the same as "zdvixqcuvd"

void pretty_printer(char *to_print, size_t size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        if (size - i > 1)
        {
            printf("%c, ", to_print[i]);
        }
        else
        {
            printf("%c", to_print[i]);
        }
    }
    printf("]\n");
}

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 3)
    {
        printf("Usage: ./insertSort [asc|dsc] to_sort\n");
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
        printf("Usage: ./insertSort [asc|dsc] to_sort\n");
        return 1;
    }
    to_sort = argv[2];

    //helpers
    int size = strlen(to_sort);
    int max;
    int index;
    
    for (int i = 0 ; i < size; i++)
    {
        //TODO
    }

    pretty_printer(to_sort, size);
    return 0;
}

