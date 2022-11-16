#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Please provide at least one Integer as arg.\n Usage: find_max INT [INT ...]~n");
    }
    int arr_len = argc-1;
    int arr[arr_len];

    for (int i = 1; i < argc; i++)
    {
        arr[i - 1] = atoi(argv[i]);
    }

    int max_index = 0;
    int max = arr[max_index];

    for (int i = 1; i < arr_len; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
            max_index = i;
        }
    }

    printf("Maximum is %i at index %i\n", max, max_index);
}