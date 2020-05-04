![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete anagrams.c
Write a Program that can intake 2 strings i.e. words and check whether they are anagrams. Checking should be outside of your main program as in the code
we provide you with. Please note that you can add the <cs50.h> library at your free will for functions such as
get_string etc. However, this is not necessary! Other than that all the Libraries you need are included in the
Header already. Make sure that your check is case sensitive i.e. that your program recognizes 'ARMY' to be a
anagram for 'mary'.

~~~
Example: Input = Army, mary; Output = Strings are anagrams
~~~
{% spoiler "Hints" %}

1. This is comparable to an evolution of a strcmpr function.
2. Think of the Letters in the alphabet and how often one letter can appear in a word.
3. Again the ASCII Table might be of help

{% endspoiler %}
