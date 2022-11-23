#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    // We have initialized your infile and outfile for you already
    FILE* infile;
    FILE* outfile;

    //ToDo
    infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("No infile found.\n");
        return 1;
    }

    outfile = fopen(argv[2], "w");
    if (outfile == NULL)
    {
        printf("No outfile found.\n");
        return 1;
    }

    char word[1024];
    char *greeting = "Name";
    while (fgets(word, 1024, infile) != 0)
    {
        if (strstr(word, greeting) != NULL)
        {
            fprintf(outfile, "Dear Mr./Mrs. %s,\n", argv[3]);
        }
        else
        {
            fprintf(outfile, "%s", word);
        }


    }

    /* To avoid a memory leak always close open files at the end
    of your program*/
    fclose(infile);
    fclose(outfile);
}
