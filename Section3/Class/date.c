#include <stdio.h>

typedef struct
{
    int day;
    int month;
    int year;
}
date;

int main(void)
{
    date d;
    d.day = 16;
    d.month = 11;
    d.year = 2022;

    printf("Today: %i.%i.%i\n", d.day, d.month, d.year);
}