#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>



void pretty_printer(char **to_print, size_t size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        if (size - i > 1)
        {
            printf("%s, ", to_print[i]);
        }
        else
        {
            printf("%s", to_print[i]);
        }
    }
    printf("]\n");
}

int strCmp(const char* s1, const char* s2)
{
    
    //TODO
    
}

char** my_merge(char **to_sort_1, char **to_sort_2, int size1, int size2, char **ret)
{
    int idx1 = 0;
    int idx2 = 0;
    while (/*TODO*/)
    {
        char *left = to_sort_1[idx1];
        char *right = to_sort_2[idx2];
        
        //TODO
        
    }
    while (size1 > idx1)
    {
        
        //TODO
        
    }
    
    //TODO

    return ret;
}

char** my_mergesort(char **to_sort, int size)
{
    
    //TODO
    
    int size_l = size/2;
    int size_r = size - size_l;
    char *left[size_l];
    char *right[size_r];

    //divide
    //TODO

    //conquer
    //TODO
}

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc < 2)
    {
        printf("Usage: ./mergeSort words to sort\n");
        return 1;
    }
    
    int size = 0;
    //TODO
    
    
    //TODO
    
    
    pretty_printer(my_mergesort(to_sort, size), size);
    return 0;
}

