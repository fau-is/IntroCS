#include <stdio.h>
#include <cs50.h>


typedef struct node
{
    int payload;
    struct node *next;
}
node;

node *create(int value);
bool add(node *list, int value);
bool find(node *list, int value);
bool delete(node *list, int value);
void print_list(node *list);

int main(int argc, char **argv)
{
    printf("Compiles\n");
}


node *create(int value)
{
    node *n = malloc(sizeof(node));

    if (n == NULL)
    {
        return NULL;
    }

    n->payload = value;
    n->next = NULL;

    return n;
}


bool add(node* list, int value)
{
    node *cursor = list;

    
}




