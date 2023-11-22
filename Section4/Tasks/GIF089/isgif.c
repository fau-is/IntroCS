#include <stdbool.h>
#include <stdio.h>

const char signature[6] = {'G', 'I', 'F', '8', '9', 'a'};

bool is_gif(FILE *f);

int main(int argc, char *argv[])
{
    // Check usage
    if (argc != 2)
    {
        printf("Usage: %s filename\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
    {
        printf("File %s not found\n", argv[1]);
        return 2;
    }

    if (is_gif(f))
    {
        printf("GIF\n");
    }
    else
    {
        printf("NoGIF\n");
    }

    fclose(f);







}

bool is_gif(FILE *f)
{
    unsigned char buffer[6];

    fread(buffer, sizeof(char), 6, f);

    for (int i = 0; i < 6; i++)
    {
        if (buffer[i] != signature[i])
            return false;
    }
    return true;
}

