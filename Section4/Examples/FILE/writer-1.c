#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>


int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s RelFilePath\n", *argv);
        return 1;
    }

    char *path = argv[1];

    FILE *file = fopen(path, "a");

    if (file == NULL)
    {
        printf("File not Found!\n");
        return 2;
    }
    printf("\n");

    while(1)
    {
        char *s = get_string("Write Line: ");

        if(strcmp(s, "") == 0)
        {
            break;
        }

        fwrite(s, strlen(s), 1, file);
        fputc('\n', file);
    }

    fclose(file);
}
