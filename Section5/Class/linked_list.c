#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    int value;
    struct node *next;
} node;

node *create(int value);
node *add(node *list, int value);
bool find(node *list, int to_find);
void delete(node *list);


int main(void)
{

}

