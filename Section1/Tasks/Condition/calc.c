#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int a = 5; // get_int("a: ");
    int b = 2; // get_int("b: ");
    int result;

    if (a > b)
    {
        result = a - b; // 3
    }
    else if (a < b)
    {
        result = a + b;
    }
    else
    {
        result = a * b; // 10
    }

    printf("%i\n", result);
}