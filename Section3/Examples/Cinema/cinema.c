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

// Cinema room
seat cinema[ROWS][ROW_LEN];


int main(void)
{

}