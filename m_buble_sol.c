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

    //helper variables
    //was there a bubble?
    bool swp = true;
    //how long do i need to follow the bubbles?
    int limit = sizeof(to_sort)/sizeof(to_sort[0]) - 1;

    //did something bubble?
    while(swp)
    {
        //not yet!
        swp = false;
        //check for bubbles
        for (int i = 0; i < limit; i++)
        {
            //do i have to sort asc or dsc?
            bool cmp;
            if(asc)
            {
                cmp = to_sort[i] > to_sort[i + 1];
            }
            else
            {
                cmp = to_sort[i] < to_sort[i + 1];
            }

            //something bubbled!
            if (cmp)
            {
                //swap the values
                int tmp = to_sort[i];
                to_sort[i] = to_sort[i + 1];
                to_sort[i + 1] = tmp;

                //remember that something bubbled
                swp = true;
            }
        }
        limit--;
    }

    pretty_printer(to_sort);
    return 0;
}