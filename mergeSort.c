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
    while(*s1 && (*s1 == *s2))
    {
        s1++;
        s2++;
    }
    return *(const unsigned char*)s1 - *(const unsigned char*)s2;
}

char** my_merge(char **to_sort_1, char **to_sort_2, int size1, int size2, char **ret)
{
    int idx1 = 0;
    int idx2 = 0;
    while (size1 > idx1 && size2 > idx2)
    {
        char *left = to_sort_1[idx1];
        char *right = to_sort_2[idx2];
        if (strCmp(left, right) <= 0)
        {
            ret[idx1 + idx2] = left;
            idx1++;
        } else
        {
            ret[idx1 + idx2] = right;
            idx2++;
        }
    }
    while (size1 > idx1) 
    {
        ret[idx1 + idx2] = to_sort_1[idx1];
        idx1++;
    }
    while (size2 > idx2)
    {
        ret[idx1 + idx2] = to_sort_2[idx2];
        idx2++;
    }

    return ret;
}

char** my_mergesort(char **to_sort, int size)
{
    if(size < 2)
    {
        return to_sort;
    }
    int size_l = size/2;
    int size_r = size - size_l;
    char *left[size_l];
    char *right[size_r];

    //divide
    for (int i = 0; i < size_l; i++)
    {
        left[i] = to_sort[i];
    }
    for (int i = size_l; i < size; i++)
    {
        right[i - size_l] = to_sort[i];
    }

    //conquer
    return my_merge(my_mergesort(left, size_l), my_mergesort(right, size_r), size_l, size_r, to_sort);
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
    for (int i = 1; argv[i] != NULL; i++, size++)
    {}
    
    char *to_sort[size];
    for (int i = 1; argv[i] != NULL; i++)
    {
        to_sort[i-1] = argv[i];
    }
    
    pretty_printer(my_mergesort(to_sort, size), size);
    return 0;
}
