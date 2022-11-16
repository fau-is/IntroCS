#include <stdio.h>
#include <string.h>


// Define count of seat rows and length of seat rows
#define ROWS 4
#define ROW_LEN 4

// Cinema seats have row, position and reserved status
typedef struct
{
    int row;
    int pos;
    bool reserved;
}
seat;

// Seating rows in the cinema are stored as a ROW x ROW_LEN matrix
seat cinema[ROWS][ROW_LEN];

// Data extracted from the online processing system
int data = {0, 1, 3, 5, 6, 8, 10, 11, 12, 13, 14, 15}

int main(void)
{
    int row;
    int pos;
    int reservation = 0;
    // populating the cinema with the data
    for (int i = 0; i < ROWS * ROW_LEN; i++)
    {
        row = data[reservation] / ROWS;
        pos = data[reservation] % ROW_LEN;

        // Accessing seat properties for seat in row ... and pos ...
        cinema[row][pos].row = row;
        cinema[row][pos].pos = pos;

        if (i == data[reservation])
        {
            cinema[row][pos].reserved = true;
            reservation++;
        }
        else
        {
            cinema[row][pos].reserved = false;
        }

    }




    for (int i = 0; i < ROWS; i++)
    {
        for (int y = 0; y < ROW_LEN; y++ )
        {

        }
    }
}