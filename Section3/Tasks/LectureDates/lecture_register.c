#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include "lecture.c"

int main()
{
    int n = get_int("How many lectures do you want to register? ");
    lecture lectures[n];

    for (int i = 0; i < n; i++)
    {
        lectures[i].day = get_int("Day: ");
        lectures[i].month = get_string("Month: ");
        lectures[i].year = get_int("Year: ");
        lectures[i].topic = get_string("Topic: ");
    }
    printf("Registered Lectures\n")

    for (int i = 0; i < n; i++)
    {
       printf("%i.%s, %i: %s\n", lectures[i].day, lectures[i].month, lectures[i].year, lectures[i].topic);
    }
}
