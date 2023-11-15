#include <stdio.h>

int main(void)
{
    int arr[] = {1, 2, 3};

    for (int i = 0; i < 3 - 1; i++)
    {
        int tmp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = tmp;
    }



    for (int i = 0; i < 3; i++)
        printf("%i ", arr[i]);
    printf("\n");

}
