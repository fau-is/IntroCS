#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

void pretty_printer(int *to_print, int size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        printf("%i, ", to_print[i]);
    }
    printf("]\n");
}

void swap(int *arr, int a, int b)
{
    int tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
}

void reheap(int *to_heap, int i, int k, int asc)
{
    int leftKid = 2 * i + 1;
    int rightKid = leftKid + 1;
    int kid;
    bool cond2 = to_heap[leftKid] > to_heap[i];
    bool cond3 = to_heap[leftKid] > to_heap[rightKid];
    if(!asc)
    {
        cond2 = !cond2;
        cond3 = !cond3;
    }
    if (leftKid <= k && rightKid > k) 
    {
        // nur ein (= linkes) Kind
        if (cond2) 
        {
            swap(to_heap, leftKid, i);
        }
    } else 
    {
        if (rightKid <= k) 
        {
            // in kidIdx groesseren der beiden Kinder erfassen
            kid = cond3 ? leftKid : rightKid;
            bool cond1 = asc ? to_heap[kid] > to_heap[i] : to_heap[kid] < to_heap[i];

            if (cond1)
            {
                swap(to_heap, i, kid);
                reheap(to_heap, kid, k, asc);
            }
        }
    }
}

void my_heapsort(int *tb_sort, int asc, int size)
{
    // build heap -> needs to be done this way!
    for (int i = size/2; i >= 0; i--)
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

int main(int argc, char **argv)
{
    int asc;

    if (argc != 2)
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }
    if (strcmp(argv[1], "asc") == 0)
    {
        asc = 1;
    }
    else if (strcmp(argv[1], "dsc") == 0)
    {
        asc = 0;
    }
    else
    {
        printf("Usage: ./bubble [asc|dsc]\n");
        return 1;
    }

    int array_length = sizeof(to_sort)/sizeof(to_sort[0]);

    my_heapsort(to_sort, asc, array_length);
    

    pretty_printer(to_sort, array_length);
    return 0;
}