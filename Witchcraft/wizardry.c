#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    //ToDo

    // We have initialized your infile and outfile for you already
    FILE* infile;
    FILE* outfile;

    //ToDo

    /* To avoid a memory leak always close open files at the end
    of your program*/
    fclose(infile);
    fclose(outfile);
}
