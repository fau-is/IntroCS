#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

int main(void)
{
    while (true)
    {
        char c = get_char("C: ");

        if (isupper(c))
        {
            printf("%i\n", c - 'A');
            c + 1000 % 26
        }
        if (islower(c))
            printf("%i\n", c - 'a');

        // Let's write a program that returns the alphabetical index
        // of a letter: e.g. A | a = 0, B = 1, C = 2, ...
    }
}
