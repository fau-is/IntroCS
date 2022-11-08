#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("String: ");

    // Use function strlen to get the number of chars in a string
    int str_len = strlen(s);

    // Create a char array with the same length as s and add 1 for \0 character
    char t[str_len + 1];

    for (int i = 0; i < str_len; i++)
    {
        t[i] = s[i];
    }

    if (strcmp(s, t) == 0)
    {
        printf("s: %s = t: %s\n", s, t);
    }
    else
    {
        printf("Strings were not equal, let's try to add '\\0' character\n");

        t[str_len] = '\0';

        if (strcmp(s, t) == 0)
        {
            printf("Now, s: %s == t: %s \n", s, t);
        }
        else
        {
            printf("%s <> %s\n", s, t);
        }
    }

    return 0;
}