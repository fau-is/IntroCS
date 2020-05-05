#include <stdio.h>
#include <ctype.h>
#include <cs50.h>

//this is the initialisation of your checker function
int anagram(char *a, char *b);
//This should be a hint in itself ;)
const int alphabet = 26;
// Max world length
const int N = 20;

int main(void)
{
    //We have initialized your strings for you already
    char a[N];
    char b[N];

    //ToDo

    return 0;
}

int anagram(char *a, char *b)
{
    // Initializing an array where you can count the letters of each word
    int a_count[alphabet];
    int b_count[alphabet];

    // Making sure you start counting from 0
    for (int i = 0; i < alphabet; i++)
    {
        a_count[i] = 0;
        b_count[i] = 0;
    }
    //ToDo
    return 0;
}



