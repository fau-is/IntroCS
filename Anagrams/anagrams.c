/*Write a Program that can intake 2 strings i.e. words and check whether they are anagrams. I.e. 'army' & 'mary' or
 * 'bored' & 'robed'. The function doing the actual checking should be outside of your main program as in the code
 * we provide you with. Please note that you can add the <cs50.h> library at your free will for functions such as
 * get_string etc. However, this is not necessary! Other than that all the Libraries you need are included in the
 * Header already. Make sure that your check is case sensitive i.e. that your program recognizes 'ARMY' to be a
 * anagram for 'mary'.
*/

#include <stdio.h>
#include <ctype.h>
//#include <cs50.h>

//this is the initialisation of your checker function
int anagram(char *a, char *b);
//As a help we have initialized a Constant for your strings
const int N = 50;
//This should be a hint in itself ;)
const int alphabet = 26;

int main(void)
{
    //We have initialized your strings for you already
    char a[N], b[N];
    //ToDo
    return 0;
}

int anagram(char *a, char *b)
{
    //ToDo
    return 0;
}



