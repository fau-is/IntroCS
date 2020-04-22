//for (int i = 0; i < 5; i++)
//  for (int j = 0; j < 5; j++)
//        printf("i = %d, j = %d\n", i, j);
// Transfer the code above into a programm that uses only one for loop instead of a double for loop
// Hint: maybe division and modulo can be helpful

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 25; i++)
    {
        printf("i = %i, j = %i\n", i / 5, i % 5);
    }
}