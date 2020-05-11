#include <stdio.h>
#include <string.h>

unsigned int MAX = 1024;

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        printf("./wizardry infile outfile name\n");
        return 1;
    }
    FILE* infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("No infile found.\n");
        return 1;
    }

    FILE* outfile = fopen(argv[2], "w");
    if (outfile == NULL)
    {
        printf("No outfile found.\n");
        return 1;
    }
    char word[MAX];
    char *greeting = "Surname";
    while (fgets(word, MAX, infile) != 0)
    {
        if (strstr(word, greeting) != NULL)
        {
            fprintf(outfile, "Dear Mr/Ms. %s\n", argv[3]);
        }
        else
        {
            fprintf(outfile, "%s", word);
        }


    }
    fclose(infile);
    fclose(outfile);
}

