#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s RelFilePath\n", *argv);
        return 1;
    }

    char *path = argv[1];

    FILE *file = fopen(path, "r"); //(r read, w write, a append)

    if (file == NULL)
    {
        printf("File not Found!\n");
        return 2;
    }
    printf("\n");

    while(!feof(file))
    {
        char c = fgetc(file);
        if (c == EOF)
        {
            continue;
        }
        printf("%c", c);
    }

    fclose(file);
    printf("\n");
}
