#include <stdio.h>

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        printf("Usage: cp source destination\n");
        return 1;
    }

    FILE *copy_file = fopen(argv[1], "r");
    FILE *dest_file = fopen(argv[2], "w");
    if(copy_file == NULL || dest_file == NULL)
    {
        printf("Could not return File.\n");
        return 1;
    }
    for(int s = fgetc(copy_file); s != EOF; s = fgetc(copy_file))
    {
        fprintf(dest_file, "%c", s);
        //putc(c, dest);
    }
    fclose(copy_file);
    fclose(dest_file);
}