#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

void countdown(int i);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recursion N\n");
        return 1;
    }

    int i = atoi(argv[1]);

    countdown(i);
}

void countdown(int i)
{
    if (i < 0)
    {
        return;
    }
    else if (i == 0)
    {
        printf("Go!\n");
        return;
    }
    printf("%i\n", i);
    countdown(i - 1);
}