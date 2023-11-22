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
        char buffer[500];
        int len = fread(buffer, sizeof(char), 500, file);
        if (len < 1)
            break;
        // buffer[len-1] = '\0';
        printf("%s", buffer);
    }

    fclose(file);
    printf("\n");
}
