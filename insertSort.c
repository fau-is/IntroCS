#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

char *to_sort = "zdvixqcuvd";
//the same as "zdvixqcuvd"

int main(int argc, char **argv)
{
    bool asc;

    if (argc != 3)
    {
        printf("Usage: ./insertSort [asc|dsc] to_sort\n");
        return 1;
    }
    if (strcmp(argv[1], "asc") == 0)
    {
        asc = true;
    }
    else if (strcmp(argv[1], "dsc") == 0)
    {
        asc = false;
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
    int idx;
    //why this way? :)
    for (int i = 0 ; i < size; i++)
    {
        max = to_sort[i];
        idx = i - 1;
        bool cond;
        if (!asc)
        {
            cond = tolower(max) > tolower(to_sort[idx]);
        }
        else
        {
            cond = tolower(max) < tolower(to_sort[idx]);
        }
        while(idx >= 0 && cond)
        {
            to_sort[idx + 1] = to_sort[idx];
            idx--;
            cond = !asc ? tolower(max) > tolower(to_sort[idx]) :
                            tolower(max) < tolower(to_sort[idx]);
        }
        to_sort[idx+1] = max;
    }

    printf("%s\n", to_sort);
    return 0;
}
