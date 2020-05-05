![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete anagrams.c
Write a Program that can intake 2 strings i.e. words and check whether they are anagrams. An anagram generally is a word or phrase
 that is formed by rearranging the letters of a different word or phrase. However, for this coding exercise don't worry about phrases.

Your Main program should only ask the User for input of 2 strings which it can compare against. Furthermore, the main function should
pass in these strings to a separate Function and only give meaning to the additional functions return values i.e. 2 strings are anagrams or not!
The Function doing the actual work i.e. checking whether 2 strings are indeed anagrams should be outside of your main program. We have already
initialized a function for you below the header and added the actual function with your ToDo below the main function. 

Please note that you can use the <cs50.h> library at your free will for functions such as
get_string() etc. However, this is not necessary! you can also use functions included in the <stdio.h> library such as fgets()!  
Make sure that your check is case in-sensitive i.e. that your program recognizes 'ARMY' to be a
anagram for 'mary'. You can find functions that will help you with this in the <ctype.h> library.
Other than that all the Libraries you need are included in the
Header already.


If unsure which library contains what function, you can find a 
Plethora of documentation for C libraries in the actual CS50 
documentation or GeekForGeeks & W3Schools.



~~~
Example: 
Input = Army, mary; 
Output = Strings are anagrams;
Input = army, arny;
Output = Strings are not anagrams;
~~~
{% spoiler "Hints" %}

1. This is comparable to an evolution of a strcmpr function.
2. Think of the Letters in the alphabet and how often one letter can appear in a word.
3. Again the ASCII Table might be of help

{% endspoiler %}
