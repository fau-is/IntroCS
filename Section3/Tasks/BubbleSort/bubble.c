#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Please provide at least one Integer as arg.\n Usage: ./bubble INT [INT ...]~n");
        return 1;
    }

    int arr_len = argc - 1;
    int arr[arr_len];

    for (int i = 1; i < argc; i++)
    {
        arr[i - 1] = atoi(argv[i]);
    }

    bool swap = true;
    int red = 1;

    while (swap)
    {
        swap = false;
        for (int i = 0; i < arr_len - red; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                swap = true;
                int tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
            }
        }
        red++;
    }
    for (int i = 0; i < arr_len; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");

        // TODO

}
