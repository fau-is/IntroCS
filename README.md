![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)
# Complete binary.c

{% video https://youtu.be/T98PIp4omUA %}

In contrast to the previous task, where you programmed a linear search approach for an unsorted array of numbers, you will now implement a binary search algorithm for a sorted array of numbers.

Like previously we provide a CS50 Lab with some starting code.
To aid you in programming, and so that you can test your solution, you can use this CS50 Lab.

Note: in the Lab, you can use the check50 command to check your solution:
~~~
$ check50 fau-is/IntroCS/CBinarySearch --local
~~~

{% next %}

# Description

For this array your program should behave in the following way.
~~~
int to_search[10] = {10, 20, 30, 40, 50, 60, 70 , 80, 90, 100};
~~~

When the number is in the array, it should print the number and the index in the following way and exit with code 0 (main returns 0):
~~~
input: ./binary 10

output: "Number 10 is at index 0"
~~~
When the number is in the array, it should print the number in the following way and exit with
 code 1 (main returns 1):
~~~
input: ./binary 3

output: "Number 3 not found"
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/CBinarySearch
~~~
