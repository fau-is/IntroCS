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
    //sorting direction
    int asc = 0;
    if (argc != 2)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }


    //TODO: check if asc or dsc
    

    //helper variables
    //was there a bubble?
    bool swp = true;
    //how long do i need to follow the bubbles?
    int limit = sizeof(to_sort)/sizeof(to_sort[0]) - 1;


    //TODO
    //HINT: which loop to you need when swp = true, which one when swp = false?


    return 0;

}