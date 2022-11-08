#include <stdio.h>
#include <ctype.h>
#include <cs50.h>

// Your main function goes below
int main(int argc, string argv[])
{
    if (argc < 3)
    {
        printf("Usage: ./addition x y");
        return 1;
    }

    int x = atoi(argv[1]);
    int y = atoi(argv[2]);

    int result = x + y;

    printf("%s + %s = %i\n", result);
}