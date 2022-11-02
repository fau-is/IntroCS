#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int a = get_int("a: ");
    int b = get_int("b: ");

    if (a > b)
    {
        printf("%i\n", a - b);
    }
    else if (a < b)
    {
        printf("%i\n", a + b);
    }
    else
    {
        printf("%i\n", a * b);
    }

}