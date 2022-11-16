#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

int main(void)
{
    while (true)
    {
        char c = get_char("C: ");

        if(isupper(c))
        {
            printf("%c\n", 'A' + ((c + 2050) - 'A') % 26);
        }
        if(islower(c))
        {
            printf("%i\n", c - 'a');
        }
    }
}