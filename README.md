![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete insertSort.c

{% video https://youtu.be/O0VbBkUvriI %}

For now the last algorithm, that you are going to program is insertion sort.

To aid you in programming, and so that you can test your solution, you can use this CS50 Lab.

Note: in the Lab, you can use the check50 command to check your solution:
~~~
$ check50 fau-is/IntroCS/CInsertionSort --local
~~~
{% next %}

# Description

This task has a slight difference. You are not going to sort an array of numbers, but a string in ascending or
descending lexicographical order.
Be careful your algorithm should work alphabetically, which means that lowercase 'c' should still be before uppercase 'Z' in ascending lexicographical order.

The usage of your program should be as follows: 
~~~
Usage: ./insertSort [asc|dsc] to_sort
~~~

to_sort is a string that only contains characters. So, don't worry about punctuation, spacing etc.

In the end, print the sorted string.

Usage examples:
~~~
./insertSort asc IntroCS
CInorSt

./insertSort dsc introcs
tsronic
~~~

**Happy Coding!**