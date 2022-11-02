#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int sum4avg = 0;
    for (int i = 0; i < 10; i++)
    {
        sum4avg += get_int("Number: ");
    }

    printf("Average: %.2f\n", sum4avg / 10.0);
}