#include <stdio.h>
#include <string.h>
#include <cs50.h>


// Define count of seat rows and length of seat rows
#define ROWS 4
#define ROW_LEN 4

// Cinema seats have row, position and reserved status
typedef struct
{
    int row;
    int pos;
    bool reserved;
    string name;
}
seat;

// Seating rows in the cinema are stored as a ROW x ROW_LEN matrix
seat cinema[ROWS][ROW_LEN];

// Data extracted from the online processing system
int data[] = {0, 1, 3, 5, 6, 8, 10, 11, 12, 13, 14, 15};
string names[] = {"Mark", "Elisa", "Jake", "Scott", "Aiden",
                  "Andrew", "Emily", "Charlotte", "Olivia",
                  "Sofia", "Adam", "Tom"};

int main(void)
{
    int row;
    int pos;
    int reservation = 0;
    // populating the cinema with the data
    for (int i = 0; i < ROWS * ROW_LEN; i++)
    {
        row = data[i] / ROWS;
        pos = data[i] % ROW_LEN;

        // Accessing seat properties for seat in row ... and pos ...
        cinema[row][pos].row = row;
        cinema[row][pos].pos = pos;

        // Checking if current seat is the next reservation
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

    // Print out rows and seat positions for all remaining free seats
    printf("Free seats:\n");
    for (int i = 0; i < ROWS; i++)
    {
        for (int y = 0; y < ROW_LEN; y++ )
        {
            if (!cinema[i][y].reserved)
            {
                printf("\tRow %i seat no %i\n", i+1, y+1);
            }
        }
    }
}