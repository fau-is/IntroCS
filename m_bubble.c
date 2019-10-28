#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

// Helper to print arrays
void pretty_printer(int *to_print);

int main(int argc, char **argv)
{
    //sorting direction
    int asc = 0;
    if (argc != 2)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }

    //TODO: check if sorting in asc (ascending) or dsc (descending) order
    

    // Some helpers
    // Limit (length of the array - 1)
    // HINT: You need to compare the ith element with the i+1th element
    int limit = sizeof(to_sort)/sizeof(to_sort[0]) - 1;
    
    // Was there a "bubble" before (Did the program swap at least two numbers), initially true
    bool swp = true;
    
    //TODO
    //HINT: Do you need a do-while or while loop when swp = true initially?
    //HINT: It might make sense to bubble values (up or down)  with a for loop
    
    
    return 0;

}

void pretty_printer(int *to_print)
{
    printf("[");
    for (int i = 0, j = sizeof(to_sort)/sizeof(to_sort[0]); i < j; i++)
    {
        printf("%i, ", to_print[i]);
    }
    printf("]\n");
}
