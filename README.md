![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete selsort.c

{% video https://youtu.be/3hH8kTHFw2A %}

Let us continue with implementing Selection Sort

To aid you in programming, and so that you can test your solution, you can use this CS50 Lab.

Note: in the Lab, you can use the check50 command to check your solution:
~~~
$ check50 fau-is/IntroCS/CSelectionSearch --local
~~~
**Note:** To make sure that you generally understood the algorithm and arrays in general, we will do it the other way
around. Instead of building up the sorted array from the left, you will build it up from the right. 

{% next %}

# Description

For this array your program should behave in the following way.
~~~
int to_search[10] = {1, 11, 4, 5, 9, 12, 55, 78, 0, 7};
~~~
If the program is called with argv[1] is equal to "asc" then it should sort the array to_sort in ascending order and print the result (a print function is provided).
~~~
./selsort asc

[2, 5, 8, 23, 33, 42, 78, 123, 2398, 4711]
~~~
If the program is called with argv[1] is equal to "dsc" then it should sort the array to_sort in descending order and print the result (a print function is provided).
~~~
./selsort dsc

[4711, 2398, 123, 78, 42, 33, 23, 8, 5, 2]
~~~