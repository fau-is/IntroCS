// Write a program which uses the cs50 get_int() function to prompt a user for a input
// Make sure that this input is between 0 - 100 print out the input Number.
//HINT: Make use of a While Loop or a do-while loop


#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("Enter Number between 0 and 100: ");
    while (n < 0 || n > 100)
    {
        n = get_int("Enter Number between 0 and 100: ");
    }
    printf("The input Number is: %d\n", n);
    return 0;
}

