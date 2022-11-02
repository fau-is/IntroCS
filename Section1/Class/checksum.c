#include <stdio.h>
#include <cs50.h>


int main(void)
{
    // Provide a number here
    int number = -1;
    do
    {
        number = get_int("Positive Number: ");  // 123 % 10 = 3; 123 / 10 = 12 % 10 = 2
                                                // 123 / 10 = 12 / 10 = 1 / 1 / 10

    }
    while (number < 0);

    int checksum = 0;

    while(number / 10 > 0 || number % 10 > 0)
    {
        int digit = number % 10;
        checksum = checksum + digit;
        number = number / 10;
    }

    printf("Checksum: %i\n", checksum);
}