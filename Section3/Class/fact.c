#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int fact(int n);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage\n");
        return 1;
    }

    int n = atoi(argv[1]);

    printf("%i\n", fact(n));
}

int fact(int n)
{
    if (n == 1)
    {
        return 1;
    }
    return n * fact(n - 1);
}