#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Text: ");
    bool palindrome = true;

	for (int i = 0, len = strlen(s); i < len / 2; i++)
	{
		if (s[i] != s[len - 1 - i])
		{
			palindrome = false;
		}
	}
	// Print output
	if (palindrome)
	{
		printf("PALINDROME\n");
	}
	else
	{
		printf("NO PALINDROME\n");
	}

}
