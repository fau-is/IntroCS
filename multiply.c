// Prompt a user for input of a number between 1-10 inclusively.
// Use a for loop with 10 iterations to multiply the number entered by the user with your initialized counter for each iteration
// printing out the numbers looking something like this: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Number between 1 and 10: ");
    }
    while (n < 1 || n > 10);

    int multiple;
    printf("[ ");
    for (int i = 0; i < 10; i++)
    {
        multiple = n*i;

        if (i != 9)
        {
            printf("%d, ", multiple);
        }
    }
    printf("%d ]\n", multiple);
    return 0;
}
