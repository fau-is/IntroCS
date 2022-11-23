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
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    char *s3 = malloc(len1 + len2 + 1);

    for (int i = 0; i < len1; i++)
    {
        s3[i] = s1[i];
    }

    for (int i = 0; i < len2; i++)
    {
        s3[len1 + i] = s2[i];
    }


    s3[len1 + len2] = '\0';
    return s3;
}
