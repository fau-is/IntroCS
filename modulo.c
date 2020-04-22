// Write a programm that prompts a user for a integer input and then tells the
// User whether the number he entered is an even number or an uneven number
// HINT: Try using the modulo operator.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("Please enter a number: ");

    int modulo = n % 2;
    if (modulo == 0)
    {
        printf("%d is an even number!\n", n);
    }
    else
    {
        printf("%d is an uneven number!\n", n);
    }
    return 0;
}
