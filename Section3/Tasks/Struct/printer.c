#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "struct.c"

int main()
{
    date dates[2];

    dates[0].year = 2021;
    dates[0].month = "December";
    dates[0].day = 6;

    dates[1].year = 2021;
    dates[1].month = "December";
    dates[1].day = 13;

    for (int i = 0; i < 2; i++)
    {
       printf("%i.%s.%i is a lecture day\n",dates[i].day, dates[i].month, dates[i].year);
    }
}
