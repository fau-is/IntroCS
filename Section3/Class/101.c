#include <stdio.h>
#include <cs50.h>

#define N 11

int main(void)
{
    int table[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            table[i][j] = (i) * (j);
        }
    }

    while (true)
    {
        int a, b;
        do
        {
            a = get_int("Index 1: ");
            b = get_int("Index 2: ");
        }
        while (a > N || a < 0 || b > N|| b < 0);

        printf("table[%i][%i] = %i\n", a, b, table[a][b]);
    }

}

