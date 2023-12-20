#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

void heapsort(int *tb_sort, int asc, int size);
void pretty_printer(int *to_print, int size);
void reheap(int *to_heap, int i, int k, int asc);
void swap(int *arr, int a, int b);

int main(int argc, char **argv)
{

    // Check usage
    if (argc != 2)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }

    // Ascending or descending
    int asc;
    if (strcmp(argv[1], "asc") == 0)
        asc = 1;
    else if (strcmp(argv[1], "dsc") == 0)
        asc = 0;
    else
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }

    int array_length = sizeof(to_sort)/sizeof(to_sort[0]);

    heapsort(to_sort, asc, array_length);

    pretty_printer(to_sort, array_length);
    return 0;
}

void heapsort(int *tb_sort, int asc, int size)
{
    // build heap -> needs to be done this way!
    for (int i = size / 2; i >= 0; i--)
    {
        reheap(tb_sort, i, size-1, asc);
    }

    // take max and reheap
    for (int i = size - 1; i > 0; i--)
    {
        //take out max
        swap(tb_sort, 0, i);

        //i points to second to last element
        reheap(tb_sort, 0, i-1, asc);
    }
}

void pretty_printer(int *to_print, int size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        if (i == size - 1)
            printf("%i]\n", to_print[i]);
        else
            printf("%i, ", to_print[i]);
    }
}

void swap(int *arr, int a, int b)
{
    int tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
}

void reheap(int *to_heap, int index, int k, int asc)
{
    // determine children indices
    int left_index = 2 * index + 1;
    int right_index = 2 * index + 2;
    bool to_heap_left = asc ? to_heap[left_index] > to_heap[index] : to_heap[left_index] < to_heap[index];
    bool to_heap_right = asc ? to_heap[left_index] > to_heap[right_index] : to_heap[left_index] < to_heap[right_index];


    if (left_index <= k && right_index > k)
    {
        // node only has left_child
        if (to_heap_left)
            swap(to_heap, left_index, index);
    }
    else
    {
        int child_index;

        if (right_index <= k)
        {
            // determine larger/lesser child index
            child_index = to_heap_right ? left_index : right_index;
            bool to_heap_at_all = asc ? to_heap[child_index] > to_heap[index] : to_heap[child_index] < to_heap[index];

            if (to_heap_at_all)
            {
                swap(to_heap, index, child_index);
                reheap(to_heap, child_index, k, asc);
            }
        }
    }
}
