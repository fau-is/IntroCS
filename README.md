![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete bubble.c

{% video https://youtu.be/RT-hUXUWQ2I %}

Now that you know how to implement some search-algorithms in C, we need to dive even deeper and start with sorting. 
In this exercise, you should implement the Bubble Sort algorithm that sorts an array of integers into either ascending 
or descending order.

To aid you in programming, and so that you can test your solution, you can use this CS50 Lab.

Note: in the Lab, you can use the check50 command to check your solution:
~~~
$ check50 fau-is/IntroCS/CBubbleSort --local
~~~

{% next %}

# Description

We use a similar array to the one in the search tasks:
~~~
int to_search[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};
~~~

**The program should behave as follows:**

If the program is called with argv[1] is equal to "asc" then it should sort the array to_sort in ascending 
order and print the result (a print function is provided).
~~~
./bubble asc

[2, 5, 8, 23, 33, 42, 78, 123, 2398, 4711]
~~~

If the program is called with argv[1] is equal to "dsc" then it should sort the array to_sort in descending order and print the result (a print function is provided).
~~~
./bubble dsc

[4711, 2398, 123, 78, 42, 33, 23, 8, 5, 2]
~~~
Print usage if the user provides neither asc nor dsc: 
~~~
./bubble asdf

Usage: ./bubble [asc|dsc]\n
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/CBubbleSort
~~~

**Have fun!**