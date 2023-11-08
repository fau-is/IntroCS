#include <stdio.h>

int main(void)
{
    int breadth = 8;

    for (int i = 1, spaces = breadth / 2 ; i <= breadth; i *= 2)
    {
        for (int j = 0; j < spaces; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
