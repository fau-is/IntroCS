#include <stdio.h>
#include <cs50.h>


int main(void)
{
    // TODO

    int number = get_int("Something");
    int sum = 0;

    while(number > 0)
    {
        sum += (number % 10);
        number = number / 10;
    }

    printf("Checksum: %i\n", sum);

}
