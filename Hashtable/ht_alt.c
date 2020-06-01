#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct node
{
    char* payload;
    struct node *next;
}
        node;

int hash(char *name)
{
    // credit to Dan Bernstein
    int c = 0;
    for (int i = 0; i < strlen(name); i++)
    {
        c += name[i] - 'a';
    }
    return c % 10;

}

bool search(char*to_search, node *hashtable[])
{
    node *trav;
    int key = hash(to_search);
    if (hashtable[key] == NULL)
    {
        return false;
    } else{
        trav = hashtable[key];
    }
    while(trav->next != NULL)
    {
        if(strcmp(trav->payload, to_search) == 0)
        {
            return true;
        }
        trav = trav->next;
    }
    return false;
}

void unload_ht(node *head)
{
    node *curr;
    while (head != NULL)
    {
        curr = head->next;
        free (head);
        head = curr;
    }
    curr = head;
    free(curr);
}


int main(void)
{
    char *A[6] = {"Chris", "Max", "Sebastian", "Johannes", "Matzner", "Chris"};
    node *hashtable[10];
    int i;
    for (i = 0; i < 10; i++)
    {
        hashtable[i] = NULL;
    }
    for (i = 0; i < 6; i++)
    {
        node *current;
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Memory allocation denied\n");
            return 1;
        }
        new_node->payload = A[i];
        new_node->next = NULL;
        int key = hash(new_node->payload);
        if (hashtable[key] != NULL)
        {
            current = hashtable[key];
            while(current->next != NULL)
            {
                current = current->next;
            }
            current->next = new_node;
        }
        else
        {
            hashtable[key] = new_node;
            //printf("%s\n", hashtable[key]->payload);
        }
    }

    char *to_search[2] = {"Chris", "Tobias"};
    for (i = 0; i < 2; i++)
    {
        if(search(to_search[i], hashtable) == true)
        {
            printf("%s exists\n", to_search[i]);
        } else{
            printf("%s does not exist\n", to_search[i]);
        }
    }
    for (i = 0; i < 10; i++)
    {
        unload_ht(hashtable[i]);
    }
    return 0;
}