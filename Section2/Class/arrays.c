#include <stdio.h>
#include <cs50.h>
#include <string.h>

const int N = 5;

int main(void)
{
    int arr[N] = {1, 2, 3, 4, 5};
    string s = "Hello";

    for (int i = 0, n = strlen(s); i < n; i++)
        printf("%c ", s[i]);
    printf("\n");
}
