#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Block 1
    int to_countdown = 0;
    do
    {
        // Block 1.1
        to_countdown = get_int("Number: ");
    } while (to_countdown <= 0);

    for(int i = to_countdown; i >= 0; i--)
    {
        printf("%i!\n", i);
    }
}