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
    printf("\nRegistered Lectures\n===============\n");

    for (int i = 0; i < n; i++)
    {
       printf("%s:\t%i.%s %i\n", lectures[i].topic, lectures[i].day, lectures[i].month, lectures[i].year);
    }
}
