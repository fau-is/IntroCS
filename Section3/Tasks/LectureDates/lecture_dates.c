#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include "struct.c"

int main()
{
    int n = get_int("How many lectures do you want to register?");
    date dates[n];

    for (int i = 0; i < n; i++)
    {
        dates[i].day = get_int("Day: ");
        dates[i].month = get_string("Month: ");
        dates[i].year = get_int("Year: ");
        dates[i].topic = get_string("Topic: ");
    }

    for (int i = 0; i < n; i++)
    {
       printf("%i.%s.%i: %s\n",dates[i].day, dates[i].month, dates[i].year, dates[i].topic);
    }
}
