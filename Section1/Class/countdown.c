#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int to_countdown = get_int("Number: ");

    for(int i = to_countdown; i >= 0; i--)
    {
        printf("%i!\n", i);
    }
}