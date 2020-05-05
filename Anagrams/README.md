![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete anagrams.c

## Anagrams
Write a Program that can intake 2 strings i.e. words and check whether they are anagrams. 
>An anagram is a word or phrase that is formed by rearranging the letters of a different word or phrase.
>For instance, rearranging the name mary can result in army. 
>Thus, these two words are anagrams of each other.

**In this exercise, don't worry about phrases. We'll just look at words.**

{% next %}
## Program Specifications
Your main function should ask the User for exactly two input strings which it will check for being anagrams to each other. 

The main function should pass these strings to the function *** int anagram(char \*a, char \*b)***.
The Function ***anagram(char \*a, char \*b)*** does the actual work, i.e. checking whether 2 strings are anagrams.

The main function should check the return value of the *anagram* function. If *anagram* returns the integer '1' the elements are anagrams, otherwise they are not.
We have already initialized a function for you below the header and added the actual function with your ToDo below the main function. 

Make sure your check is case in-sensitive i.e. that your program recognizes "ARMY" to be an anagram for "mary".
~~~
Example (anagram): 
Input = "Army", "mary" 
Output = "Strings are anagrams\n"
~~~
~~~
Example (not an anagram):
Input = "red", "blue"
Output = "Strings are not anagrams\n"
~~~

{% next "Library Talk" %}

## Libraries
Note that you can use the <cs50.h> library at your free will for functions such as
get_string() etc. However, this is not necessary! you can also use functions included in the <stdio.h> library such as fgets()!. 
You find functions that will help you with this task in the *ctype.h* library.
Other than that all the libraries you need are included in the header already.

If you don't know which library contains what function, you find a plethora of documentation for C libraries in the actual CS50 documentation, GeekForGeeks and W3Schools.

{% next "Spoiler: Algorithmic approach" %}
***Note***: This is only one way to the solution, there are many more. 
In Computer Science we often don't have the one and greatest sample solution. 
If you have an own idea how to solve the task, then we encourage you to follow your own path.

The general idea of this task is to let you count the number of each alphabetical letters in both words.

~~~
Example:
Input: Army, Mary
Army | Mary (letter counts in alphabetical order):
	1a	|	1a
	0b	|	0b
	0c	|	0c
	...	|	...
	0l	|	0l
	1m	|	1m
	0n	|	0n
	...	|	...
	0q	|	0q
	1r	|	1r
	0s	|	0s
	...	|	...
	0x	|	0x
	1y	|	1y
	0z	|	0z
**Note**: As you can see anagrams will always have the exact same number of each letter in the alphabet.
~~~

## The Alphabetical Index
Use the alphabetical index to count the number of letter occurrences.
You get the alphabetical Index for an upper-case letter by subtracting 'A' from the upper-case letter.
You get the alphabetical index for a lower-case letter by subtracting 'a' from the lower-case letter. 
Look at the ascii table and try it out you'll see that it works. As a consequence :
~~~
Alphabetical index
A, a = 0
B, b = 1
C,c = 2
...
Z,z = 25
~~~ 

## Pseudo Code
The algorithmic approach might sound as follows: 

~~~
1. Count letters in word *a*:
	- Iterate over the word and look at the letter:
		- check if letter is lower or upper case
		- get alphabetical index
		- in the array a_count add 1 at the obtained alphabetical index
2. Count letters in word *b*:
	- Repeat procedure of word a for word b. 
3. Check whether the arrays a_count and b_count are equal:
	- Iterate over the arrays with a loop that covers the whole alphabet
		- Compare the values of a_count[i] and b_count[i]
		- if they are not similar return 0 (the words aren't anagrams 
	- If you came across the iteration you can return 1 (the words are anagrams)
~~~
## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset2/Anagrams --local
~~~

