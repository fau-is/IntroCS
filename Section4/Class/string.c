#include <stdlib.h>
#include <stdio.h>


int main(void)
{
    char *s = "Hello";
    char t[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

    char *u = malloc(sizeof(char) * 100);

    scanf("%s %s\n", u);

    printf("%s\n", u);


}