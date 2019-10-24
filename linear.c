#include <stdio.h>
#include <stdlib.h>

int to_search[10] = {1, 11, 4, 5, 9, 12, 55, 78, 0, 7};

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: ./linear Number");
        return 1;
    }
    int to_find = atoi(argv[1]);
    int array_length = sizeof(to_search)/sizeof(to_search[0]);
    // TODO
}
