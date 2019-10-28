#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void pretty_printer(int *to_print, size_t size);
void swap(int *arr, int a, int b);
void reheap(int *to_heap, int i, int k, int asc);
void my_heapsort(int *tb_sort, int asc, size_t size);

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};


int main(int argc, char **argv)
{
    int asc;

    if (argc != 2)
    {
        printf("Usage: ./heapSort [asc|dsc]\n");
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
        printf("Usage: ./heapSort [asc|dsc]\n");
        return 1;
    }

    //TODO: how to determine the array_length?

    my_heapsort(to_sort, asc, array_length);

    pretty_printer(to_sort, array_length);
    return 0;
}

void my_heapsort(int *tb_sort, int asc, size_t size)
{

    //TODO
    // build heap


    //TODO
    // take out max and reheap
    

}

void swap(int *arr, int a, int b)
{
    //TODO
}

//ascending?
//k -> here the sorted part starts, better not to touch
//i -> maybe you should sink the element at this index into the heap
void reheap(int *to_heap, int i, int k, int asc)
{
    //helper: remember the structure of a heap
    int leftKid = 2 * i + 1;
    int rightKid = leftKid + 1;
    int kid;
    

    //TODO: here you can take car of the asc/dsc part


    if (leftKid <= k && rightKid > k) 
    {
        

        //TODO


    } else 
    {
        

        //TODO


    }
}

void pretty_printer(int *to_print, size_t size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        if (i == size - 1)
        {
            printf("%i", to_print[i])   
        }
        else
        {
            printf("%i, ", to_print[i]);
        }
    }
    printf("]\n");
}
