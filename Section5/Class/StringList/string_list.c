#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct node
{
    char *value;
    struct node *next;
}
node;

node *create(char *value);
node *add(node *list, char *value);
bool find(node *list, char *value);
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

    char *buffer[100];
    node *list;

    while(fscanf(f, "%s", read) == 1)
    {
        list = add(list, i);
        if (list == NULL)
        {
            break;
        }
    }

    fclose(f);

    print_list(list);
    delete(list);
}


node *create(char *value)
{
    node *n = malloc(sizeof(node));

    if (n == NULL)
    {
        return NULL;
    }

    n->value = value;
    n->next = NULL;

    return n;
}


node* add(node *list, char *value)
{
    if (list == NULL)
        return create(value);

    node *new = create(value);
    if (new != NULL)
    {
        new->next = list;
        return new;
    }
    return list;
}


bool find(node *list, int value)
{
    for (node* cursor = list; cursor != NULL; cursor = cursor->next)
    {
        if (cursor->value == value)
        {
            return true;
        }
    }
    return false;
}

bool delete(node *list)
{
    if (list == NULL)
        return true;
    delete(list->next);
    free(list);
    if(list == NULL)
        return true;
    return false;
}


void print_list(node *list)
{
    printf("->");

    for (node *cursor = list; cursor != NULL; cursor = cursor->next)
    {
        printf("%s->", cursor->value);
    }
    printf("\n");
}



