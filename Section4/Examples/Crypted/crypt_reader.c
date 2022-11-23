#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s RelFilePath\n", *argv);
        return 1;
    }

    char *path = argv[1];

    FILE *file = fopen(path, "r");

    if (file == NULL)
    {
        printf("File not Found!\n");
        return 2;
    }

    while(!feof(file))
    {
        char c = fgetc(file);
        if (c == EOF)
        {
            continue;
        }
        printf("%c", c);
        fseek(file, 3, SEEK_CUR);
    }

    fclose(file);
    printf("\n");
}
