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

    // Open file
    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("File not Found!\n");
        return 2;
    }

    // Check for GIF signature
    if (is_gif(file))
    {
        printf("GIF\n");
    }
    else
    {
        printf("NOT GIF\n");
    }

    // Close file

}

bool is_gif(FILE *f)
{
    // Read bytes in to buffer
    unsigned char buffer[6];
    int bytes = fread(buffer, 1, 6, f);

    // Check number of bytes read
    if (bytes != 6)
    {
        return false;
    }

    // Check each byte
    for (int i = 0; i < 6; i++)
    {
        if (buffer[i] != signature[i])
        {
            return false;
        }
    }

    return true;
}

