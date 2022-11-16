#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Please provide at least one Integer as arg.\n Usage: ./bubble INT [INT ...]\n");
        return 1;
    }

    int arr_len = argc - 1;
    int arr[arr_len];

    for (int i = 1; i < argc; i++)
    {
        arr[i - 1] = atoi(argv[i]);
    }
    // TODO

    for (int i = 0; i < arr_len; i++)
    {
        bool swap = false;
        for (int j = 0; j < arr_len - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
                swap = true;
            }
        }
        if (!swap)
            break;
    }

    printf("[");
    for (int i = 0; i < arr_len; i++)
    {
        if (i == arr_len-1)
            printf("%i]\n", arr[i]);
        else
            printf("%i, ", arr[i]);
    }
}