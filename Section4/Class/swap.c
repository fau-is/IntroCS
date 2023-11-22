#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


int main(void)
{
    int a = 5;
    int b = 6;

    swap(&a, &b);

    printf("a: %i b: %i\n", a, b);

}
