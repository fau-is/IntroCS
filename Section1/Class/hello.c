// Everyone's first ever program hello.c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("How many times: ");
    } while(n > 5 || n < 1);

    string name = get_string("What's your name?");

    for(int i = 0; i < n; i++)
    {
        printf("%i: Hello, %s!\n", i, name);
    }
}
