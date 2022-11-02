#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int a = get_int("A: ");
    int b = get_int("B: ");
    int result = 0;

    if (a > b)
    {
        result = a - b;
    }
    else if (a < b)
    {
        result = a + b;
    }
    else
    {
        result = a * b;
    }

    printf("a: %i; b: %i; result %i\n", a, b, result);

}
