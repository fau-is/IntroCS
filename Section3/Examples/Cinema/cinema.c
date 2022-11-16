#include <stdio.h>

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
    
}