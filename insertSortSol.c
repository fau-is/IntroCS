#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 3)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
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
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }
    to_sort = argv[2];

    //helpers
    int size = strlen(to_sort);
    int max;
    int idx;
    //why this way? :)
    for (int i = 0 ; i < size; i++)
    {
        max = to_sort[i];
        idx = i - 1;
        bool cond = !asc ? max > to_sort[idx] : max < to_sort[idx];
        while(idx >= 0 && cond)
        {
            to_sort[idx + 1] = to_sort[idx];
            idx--;
            cond = !asc ? max > to_sort[idx] : max < to_sort[idx];
        }
        to_sort[idx+1] = max;
    }

    printf("%s\n", to_sort);
    return 0;
}
