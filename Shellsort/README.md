---
files: [shellsort.c]
window: [terminal]
---
![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)
# Complete shellsort.c

## ShellSort
In this Exercise you will learn about ShellSort and write some code for yourself.

**Before you start to code watch the video and read the explanations carefully. We want you 
to understand and apply concepts rather than blindly applying them.**

{% next %}
## ShellSort Explanation
{% video https://www.youtube.com/watch?v=ddeLSDsYVp8 %}

## Specification
As you might have noticed we have provided you with some starter code and some
complete functions for you to work with. In the following we will explain the functions
and specify what we want you to do.

{% next %}

## int main(void)

***Note***: You do not need to write any code here.

The main function of the program initializes the integer array "A[]". Next
we also calculate the size of the array with our initialized integer "size".

After taking these steps we pass our array and its size into our actual sorting algorithm
specified through the function "shellsort"

After the algorithm finished its work it will return a sorted array to your main
function. The main function then proceeds to pass in the sorted array "A[]" and "size"
into a printer function which prints out the array. 

{% next %}

## void shellsort(int A[], int size)

This is where you need to start coding. Try applying the technique behind ShellSort 
through your code. 

Remember that ShellSort is similar to a insertion_sort. This means that the only
difference is that the compared values have a crescent/gap between them which you need
to take into account.

{% next %}

## void pretty_printer(int A[], in z size)

This function will print out your array at the end of your program.

## Libraries
As you might have noticed we have written all of the required libraries for you into the header
of your program.

However, if you don't know which library contains what function, you find a plethora of documentation for
C libraries in the actual CS50 documentation, GeekForGeeks and W3Schools.

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/CAlgorithms/Shellsort --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/CAlgorithms/Shellsort
~~~

**Have fun coding!**
