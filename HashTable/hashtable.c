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

node *hashtable[10];

int hash(char *name)
{
    //ToDo Hash function
    //return integer;
}

bool search(char*to_search, node *hashtable[])
{
    //ToDo
    //return true or false;
}

void unload_ht(node *head)
{
    //ToDo
}


int main(void)
{
    char *A[6] = {"Harth", "Max", "Sebastian", "Johannes", "Matzner", "Chris"};
    int i;
    for (i = 0; i < 10; i++)
    {
        hashtable[i] = NULL;
    }

    //ToDo Load the Hashtable

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

