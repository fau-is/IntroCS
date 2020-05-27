#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct node
{
    unsigned char* payload;
    struct node *next;
}
        node;

unsigned int hash(unsigned char *name)
{
    // credit to Dan Bernstein
    unsigned int hash = 10;
    int c;

    while (c = *name++)
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }
    return hash % 10;
}

bool search(unsigned char*to_search, node *hashtable[])
{
    node *trav;
    unsigned int key = hash(to_search);
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
    unsigned char *A[6] = {"Harth", "Max", "Sebastian", "Johannes", "Matzner", "Chris"};
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
        unsigned int key = hash(new_node->payload);
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

    unsigned char*to_find = "Chris";
    unsigned char*to_find1 = "Tobias";
    if(search(to_find1, hashtable) == true)
    {
        printf("%s exists\n", to_find1);
    } else{
        printf("%s does not exist\n", to_find1);
    }
    for (i = 0; i < 10; i++)
    {
        unload_ht(hashtable[i]);
    }
    return 0;
}

