#include <stdio.h>
#include <stdlib.h>

int to_search[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: ./binary Number\n");
        return 1;
    }
    int to_find = atoi(argv[1]);
    int array_length = sizeof(to_search)/sizeof(to_search[0]);
    
    // Helpers
    // Initial index of first element
    int first = 0;
    //Initial index of last element
    int last = array_length - 1;
    // Initial middle
    int middle = last / 2; 
    
    // TODO Iterative Binary Search 
    // Hint: Maybe a while loop helps
    
    
    printf("Number %i not found\n", to_find);
    return 1;

}
