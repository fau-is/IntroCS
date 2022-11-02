#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int a = get_int("a: ");
    int b = get_int("b: ");
    int result;
    
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

    printf("%i\n", result);
}