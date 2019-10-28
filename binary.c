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
    
    int start = 0;
    int end = array_length - 1;
    int middle = end / 2; 
    
    // As long as the last element to examine is equal 
    // or lower than the first element proceed 
    while (start <= end)
    {
        if (to_find == to_search[middle])
        {
            // If number is found print and return 0
            printf("Number %i is at index %i\n", to_find, middle);
            return 0;
        }
        else if (to_find < to_search[middle])
        {
            // Set last as middle -1, persuing on the side with minor numbers
            // - 1 because we know it's not the number at present middle
            end = middle - 1;
        }
        else if (to_find > to_search[middle])
        {
            // Set first as middle +1, persuing on the side with major numbers
            // + 1 Because we know already it's not the number at present middle
            start = middle + 1;
        }
        // Reset the middle variable
        middle = (start + end) / 2; 
    }
    
    printf("Number %i not found\n", to_find);
    return 1;
}
