#include <stdio.h>
#include <string.h>
#include <stdlib.h>
const int MAX 1024;

int count_lines(char *file)
{
    FILE *cities;
    cities = fopen("cities.txt", "r");
    if(cities == NULL)
    {
        printf("File is empty\n");
        return 1;
    }
    int counter = 1;
    char c = getc(cities);
    while (c != EOF)
    {
        //Count whenever new line is encountered
        if (c == '\n')
        {
            counter++;
        }
        //take next character from file.
        c = getc(cities);
    }
    fclose(cities);
    return counter;
}

char ** create_array(int size, char *file)
{
    char A[size][MAX];
    FILE *cities = NULL;
    int i = 0;
    int total;
    cities = fopen(file, "r");
    while(fgets(A[i], MAX, cities))
    {
        A[i][strlen(A[i]) - 1] = '\0';
        i++;
    }
    fclose(cities);

    total = i;

    for(i = 0; i < total; ++i)
    {
        printf("%s\n", A[i]);
    }
    return A;
}

int main(void)
{
    char *file = "cities.txt";
    int size = count_lines(file);
    printf("this is the size: %i\n", size);
    char A[size][MAX] = create_array(size, file);
    return 0;
}