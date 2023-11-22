#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char *concatenate(char *s1, char *s2);

int main(void)
{
    char *s1 = get_string("s1: ");
    char *s2 = get_string("s2: ");

    char *s3 = concatenate(s1, s2);
    printf("%s\n", s3);
    free(s3);
}
// "Hello " "World" => "Hello World"
char *concatenate(char *s1, char *s2)
{
    int size = strlen(s1) + strlen(s2) + 1;

    char *p = malloc(size * sizeof(char));

    if (p == NULL)
    {
        return "";
    }

    for (int i = 0, j = strlen(s1); i < j; i++)
        p[i] = s1[i];

    for (int i = 0, j = strlen(s1); j < size - 1; i++, j++)
        p[j] = s2[i];

    p[size] = '\0';


    return p;
}
