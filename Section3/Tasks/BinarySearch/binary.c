#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Please provide at least one Integer as arg.\n Usage: ./binary INT [INT ...]~n");
        return 1;
    }

    int arr_len = argc - 1;
    int arr[arr_len];

    for (int i = 1; i < argc; i++)
    {
        arr[i - 1] = atoi(argv[i]);
    }

    bool is_sorted = true;

    for (int i = 0; i < arr_len - 1; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            is_sorted = false;
        }
    }
    if (!is_sorted)
    {
        printf("Please provide Integers in ascending order!\n");
        return 2;
    }
    // TODO

    

}