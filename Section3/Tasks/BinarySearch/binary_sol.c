#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

bool binary_search(int start, int end, int to_find, int arr[]);

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

    int to_find = get_int("To Find: ");

    if (binary_search(0, arr_len-1, to_find, arr))
        printf("Found\n");
    else
        printf("Not Found\n");



}

bool binary_search(int start, int end, int to_find, int arr[])
{
    if (end < start)
    {
        return false;
    }

    int middle = (start + end) / 2;

    if (to_find == arr[middle])
    {
        return true;
    }
    else if(to_find > arr[middle])
    {
        return binary_search(middle + 1, end, to_find, arr);
    }
    else
    {
        return binary_search(start, middle - 1, to_find, arr);
    }



}