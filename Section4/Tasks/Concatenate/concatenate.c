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
    return "";
}
