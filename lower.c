/*Write a Program that can read a given Array of chars and convert capitalized letters into non capitalized letters
 * and vice versa. Make sure that should you loop your program has an included function that always calculates the size
 * of your array! The output for the given array should look as follows: "[ a, B, c, D, e, F ]"
 * HINT: Try looking at the Ascii table and use functions included in the ctype.h library*/

#include <stdio.h>
#include <ctype.h>

char array[] =  { 'A', 'b', 'C', 'd', 'E', 'f' };

int main(void)
{
    int size = sizeof(array)/sizeof(char);
    printf("[ ");
    for (int i = 0; i < size; i++)
    {
        if(array[i] - 32 == toupper(array[i]))
        {
            array[i] = toupper(array[i]);
        }
        else
        {
            array[i] = tolower(array[i]);
        }

        if(i < size - 1)
        {
            printf("%c, ", array[i]);
        }
    }
    printf("%c ]\n", array[size-1]);
    return 0;
}
