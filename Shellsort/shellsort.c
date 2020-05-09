#include <stdio.h>

int shellsort(int A[], int size);
void pretty_printer(int A[], int size);

int main(void)
{
    int A[] = {3, 4, 9, 10, 2, 1, 7, 5, 6, 8};
    int size = sizeof(A) / sizeof(int);

    shellsort(A, size);
    pretty_printer(A, size);
    return 0;
}

int shellsort(int A[], int size)
{
    //ToDo
}

void pretty_printer(int A[], int size)
{
    printf("[ ");
    int k;
    for (k = 0; k < size; k++)
    {
        if (k != size - 1)
        {
            printf("%i, ", A[k]);
        }
    }
    printf("%i ]", A[k]);
}

