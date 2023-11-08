#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

const int LENGTH_ARRAY = 3;

int main(int argc, string argv[])
{
    N = 2;
    if (argc < 2)
    {
        printf("Usage: %s n [N]\n", argv[0]);
        return 1;
    }

    int scores[argc-1];

    for (int i = 0; i < argc-1; i++)
    {
        scores[i] = atoi(argv[i + 1]);
    }


    int sum = 0;

    for (int i = 0; i < argc-1; i++)
        sum += scores[i];

    printf("%i\n", sum);

}
