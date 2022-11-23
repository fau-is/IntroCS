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

}

