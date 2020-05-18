![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete linear.c

{% video https://www.youtube.com/watch?v=TwsgCHYmbbA %}

Program the linear search algorithm for an array of numbers. 
For simplicity reasons in this example,  we use a fixed array with ten numbers!

The number that you need to search is given via the command-line. 
The conversion of the argument is already implemented, so you only need to program a linear search algorithm.

To aid you in programming, and so that you can test your solution, you can use this CS50 Lab.

Note: in the Sandbox, you can use the check50 command to check your solution:
~~~
$ check50 fau-is/IntroCS/CLinearSearch --local
~~~

{% next %}

# Description

For this array your program should behave in the following way.
~~~
int to_search[10] = {1, 11, 4, 5, 9, 12, 55, 78, 0, 7};
~~~

When the number is in the array, it should print the number and the index in the following way and exit with code 0 (main returns 0):
~~~
input: ./linear 11

output: "Number 11 is at index 1"
~~~
When the number is in the array, it should print the number in the following way (main returns 1):
~~~
input: ./linear 3

output: "Number 3 not found"
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/CLinearSearch
~~~