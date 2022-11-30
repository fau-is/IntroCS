#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct node
{
    int value;
    struct node *next;
}
node;

node *create(int value);
node *add(node *list, int value);
bool find(node *list, int value);
int size(node *list);
bool delete(node *list);
void print_list(node *list);

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s filepath\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
    {
        printf("Path %s does not exist\n", argv[1]);
        return 2;
    }

    int i;
    node *list;

    while(fscanf(f, "%i", &i) == 1)
    {
        list = add(list, i);
        if (list == NULL)
        {
            break;
        }
    }

    fclose(f);
    print_list(list);
    printf("%i numbers were read.\n", size(list));
    delete(list);
}


node *create(int value)
{
    node *new = malloc(sizeof(node));

    if (new != NULL)
    {
        new->value = value;
        new->next = NULL;
    }
    return new;
}


node *add(node *list, int value)
{
    node *new = create(value);
    if (list == NULL)
    {
        return new;
    }
    else
    {
        new->next = list;
    }
    return new;




    return NULL;
}


bool find(node *list, int value)
{
    return false;
}

bool delete(node *list)
{
    return false;
}

int size(node *list)
{
    return 0;
}


void print_list(node *list)
{
    printf("->");

    for (node *cursor = list; cursor != NULL; cursor = cursor->next)
    {
        printf("%i->", cursor->payload);
    }
    printf("\n");
}



