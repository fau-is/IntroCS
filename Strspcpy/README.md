![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

# Strspcpy
> This is a guided task.

The task practices how to use modulo to iterate over the same array multiple times within a single loop. 

The task might be particularly helpful if you struggle with vigenere.
## Task description
First things first, we are going to code a special string copy. The programs name is strspcpy.
The program receives exactly two command-line inputs:
1. **n**: an integer that specifies the length of the output (min 1 and max 50).
2. **to_copy**: the source string that we want to copy. The string may only consist of alphabetical character.

The program should create a new string that is _n_ characters long. It should fill the string 
with the chars from *to_copy* as long as they fit in.

```
Examples:
1)
    ./strspcpy 3 a
    > aaa
2)
    ./strspcpy 7 abc
    > abcabca
3)
    ./strspcpy 2 Hello
    > He
```

The interesting thing about this task is that we must iterate over the input string and the output string at the same time.
The loop variable for the output string might be a higher number than the input string's length.

Take a look at example 1). If we set up a loop to run from 0 to 3 we are at the end of the string "a" after the first iteration.

You can either do the task on your own them you do not need to proceed further. If you don't feel confident enough then follow
our walkthrough. It will finally take you to our solution for strspcpy.
 
{% next "Walkthrough /w Solutions" %}
## Walkthrough /w Solutions

### The header

As in most programming tasks we first need to ensure that we include the right libraries on top:
- printf() => stdio.h (Standard in and output library) to print the solution
- atoi() => stdlib.h (Standard C library) converts the command line arg to an integer
- strlen() => string.h (string library) gets the length of the input string
- isalpha() => ctype.h (Character type library) to check wheter a char is alphabetical

Add these libraries to your strspcpy.c file as the header.
If you don't remember how click the button to see how it's done:

{% spoiler "Header in C-Code" %}
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```
{% endspoiler %}

### The main function

The main function enables running a file as a program.
If you don't have a main function you cannot call your program from the command-line.

_Side notice_: Source code that does not contain a main function, but provides a set of functions that other programs use are called libraries.

Declaring a main function always follows the same pattern. The main function returns an integer that indicates whether the program
ran successfully or not. Remember: a '0' means successful and any non-zero value means there is an error.

The main function receives two parameters:
- _int argc_: the argument count
- _char **argv_: the argument vector

Declare your main function now. Pay attention to your style, i.e. no spaces between round paranthesis and the function name,
the curly parentheses follow in the next line, after the comma that separates the function parameters follows a blank space. 

If you're done have a look here: 

{% spoiler "Main" %}
```C
int main(int argc, char **argv)
{
    //ToDo
} 
```
{% endspoiler %}

{% next "Input" %}

Good job! Remember, these steps will be quite similar for any C Program that you write in your programming career.
 
### The input
Let's presume checking the command line input since we already have a compiling C-Program.

#### The number of arguments
First, let's check whether the number of input arguments is correct. 
Argc the argument count delivers the number of arguments provided to your program. 

Remember that argc always includes your program name too. Thus, if we want to get 2 arguments like in this case
we must check whether argc equals 3 instead of 2. 
If argc is not 3 the program should return the error code 1 and the program ends. Otherwise it proceeds.

Implement an if-statement that checks whether argc is three or not. 
Pay attention to your style.

**You may not use an else.**

{% spoiler "argc check" %}
```c
int main(int argc, char **argv)
{
    if (argc != 0)
    {
        return 1;
    }
    // Proceed
}
```

{% endspoiler %}

#### n 
The first command-line argument is an integer _n_ representing the length of our output string. 
There are three things that need to be done with n: 
1. Get it from the argument vector (At which place is it?)
2. Convert it to an integer
3. Check whether the integer meets our condition (min. 1 max 50)

We will leave 1. open to you, you should be able to figure this out all by yourself. 

Regarding 2., the function atoi() receives a string as parameter and tries to parse an integer from the string.
The procedure returns 0, if the string cannot be parsed. Thus, there is no need to check the characters in our case.
Store the return value of atoi in a newly declared _int n_.

Last, check if n is smaller than 1 or larger than 50. In this case, abort the program and return the exit code "2".
 
 Try to meet these specifications by yourself. If you want check our solution: 
 
{% spoiler "Check n" %} 
```c
int main(int argc, char **argv)
{
    if (argc != 0)
    {
        return 1;
    }
    
    int n = atoi(argv[1]);
    if (n < 1 || n > 50)
    {
        return 2;
    }
}
```
{% endspoiler %}
 
 #### to\_copy
 
 For to_copy we need to conduct the following steps:
 1. Get it from the command line (argv)
 2. Get its length (strlen(string))
 3. Iterate over the string and check every character whether it's an alphabetical char (isalpha())
 
 Get the string from argv and store it in **char \*to\_copy**. Then, call strlen with to_copy as a parameter and store
 the return value in **int len**. 
 
 Write a for-loop that iterates from 0 to _len_. In each iteration check each character with an if-statement. 
 If the character at place i in to_copy is not alphabetical. In this case your program returns 3. 
 Otherwise, it just goes on.
 
 **Note**: isalpha receives one parameter, a char. It returns 0, if the character is not alphabetical, and a non-zero value if
 it is not alphabetical.

 
 {% spoiler "Check to_copy" %}
```c
int main(int argc, char **argv)
{
    if (argc != 0)
    {
        return 1;
    }
    
    int n = atoi(argv[1]);
    if (n < 1 || n > 50)
    {
        return 2;
    }

    char *to_copy = argv[2];
    int len = strlen(to_copy);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(to_copy[i]) == 0)
        {
            return 3;
        }
    }
}
```
{% endspoiler %}
 
**Nice we are done with the program input and can now start to special copy. If anything is unclear up to now, please let us know via Teams!**
___
### Algorithm

Now, we get to the more interesting parts of this task.

#### copy destination
To proceed we first need to set up a new string that we can copy to. 
String intuitions: 
- strings are arrays of chars
- the difference between a char array, and a string is the so-called end-of-string character '\0'.

1. Create a char array of size (_n_ + 1) named _copy\_dest_.
2. At the last place of the created char array set the char to '\0'.

The reason why we add 1 to n is that we can add the end of string character.

Remember that computer scientists count starting from 0. So, the last place of an array of size n + 1 will be n.

{% spoiler "Check copy_dest" %}

```c
int main(int argc, char **argv)
{
    if (argc != 0)
    {
        return 1;
    }
    
    int n = atoi(argv[1]);
    if (n < 1 || n > 50)
    {
        return 2;
    }

    char *to_copy = argv[2];
    int len = strlen(to_copy);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(to_copy[i]) == 0)
        {
            return 3;
        }
    }

    char copy_dest[n+1];
    char copy_dest[n] = '\0';
}
```

 {% endspoiler %}
 
 {% next "The loop" %}
 #### Creating the Copy Loop
 
 We're almost finished. All we need to do is to loop from 0 to _n_ using int i as iterator over the output string.
 Add the char at place _i_ modulo (%) _len_ in _to\_copy_ to _copy\_dest_ at place _i_.
 
 Modulo len: We use modulo len to get a place in the string that actually exists. 
 Modulo will give you the remainder of a division. _len_ is exactly 1 greater than the last index of 
 str. So the maximum number that modulo by _len_ returns is _len_-1 (= last index in to_copy) and 0.
 
 Try to implement that loop.
 
 {% spoiler "Loop" %}

```c
int main(int argc, char **argv)
{
    if (argc != 0)
    {
        return 1;
    }
    
    int n = atoi(argv[1]);
    if (n < 1 || n > 50)
    {
        return 2;
    }

    char *to_copy = argv[2];
    int len = strlen(to_copy);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(to_copy[i]) == 0)
        {
            return 3;
        }
    }

    char copy_dest[n+1];
    char copy_dest[n] = '\0';
    
    for (int i = 0; i < n; i++)
    {
        copy_dest[i] = copy_dest[i % len];
    }
}
``` 

 {% endspoiler %}
 
 {% next "Output" %}
 ### Output
 If you have done that we finally come to the output. 
 We will simply print the copy_dest to the command-line using printf().
 
 Remember that printf gets as first parameter the format of what you want to print.
 You need placeholder for a type of variable that you want to print. 
 
 The following parameters must match the format you specified. 
 
 "%s" is the placeholder for a string variable. _copy\_dest_ is what you want to print.
 Be sure that you finish with a new line '\n'.
 
 Write that last line of code and we are done.
 
{% spoiler "Complete Solution" %}
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main(int argc, char **argv)
{
    if (argc != 0)
    {
        return 1;
    }
    
    int n = atoi(argv[1]);
    if (n < 1 || n > 50)
    {
        return 2;
    }

    char *to_copy = argv[2];
    int len = strlen(to_copy);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(to_copy[i]) == 0)
        {
            return 3;
        }
    }

    char copy_dest[n+1];
    copy_dest[n] = '\0';
    
    for (int i = 0; i < n; i++)
    {
        copy_dest[i] = copy_dest[i % len];
    }
    
    printf("%s\n", copy_dest);
}   
```

{% endspoiler %}

{% next "Check50" %}

## Check50

To see if you've done everything right run: 

> check50 fau-is/IntroCS/Pset2/Strspcpy

If there are all greens and smiles you've done everything right!
Perfect!

If there are frowns, double check what you might have missed.
 