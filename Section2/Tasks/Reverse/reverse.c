#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Text: ");

    for (int i = 0, n = strlen(s); i < n; i++)
        printf("%c", s[n-i-1]);
    printf("\n");


    return 0;
}
