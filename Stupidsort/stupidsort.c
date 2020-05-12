#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void stupidsort(int A[], int size);
bool array_sorted(int A[], int size);
void randomize(int A[], int size);
void pretty_printer(int A[], int size);

int main() {
    int A[] = {5, 7, 8, 9, 6, 3, 4, 2, 3, 1};
    int size = sizeof(A)/sizeof(int);
    stupidsort(A, size);
    pretty_printer(A, size);
    return 0;
}

void stupidsort(int A[], int size)
{
    //ToDo
}

bool array_sorted(int A[], int size)
{
    //ToDo
}

void randomize(int A[], int size)
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
    printf("%i ]\n", A[k]);
}


