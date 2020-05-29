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

node *hashtable[10];

unsigned int hash(unsigned char *name)
{
    //ToDo Hash function
    //return unsigned int;
}

bool search(unsigned char*to_search, node *hashtable[])
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
    unsigned char *A[6] = {"Harth", "Max", "Sebastian", "Johannes", "Matzner", "Chris"};
    int i;
    for (i = 0; i < 10; i++)
    {
        hashtable[i] = NULL;
    }

    //ToDo Load the Hashtable

    unsigned char *to_search[2] = {"Chris", "Tobias"};
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

