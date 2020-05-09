![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete stupidsort.c

## StupidSort
Hey all you cool cats and kittens! 

In this Exercise you will learn about StupidSort and write some code for yourself.

**Before you start to code read the specifications and explanations carefully. We want you 
to understand and apply concepts rather than blindly applying them.**

{% next %}
## StupidSort Explanation
StupidSort in its essence is a sorting algorithm which takes an unsorted array and sorts it.
~~~
Example: 
Input = [ 10, 5, 7, 3, 2, 4, 8, 9, 1, 6 ] 
Output = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
~~~
Now you might be wondering why StupidSort is actually called "Stupid". This sorting algorithm comes
with many names. For example it is also called (most commonly actually) Bogosort, Alexsort and even 
Monkeysort. 

However, enough with the name dropping and back to the fun stuff. StupidSort is called
the way it is because it sorts an array not following a clear sorting structure. This algorithm 
actually randomizes all values included in an array until it by chance has randomized the array 
in the correct order.

Now all of you programmers will now think to yourself "This is not effective!". And to that we say: "Well you are 
of course absolutely right!" This sorting procedure is actually an unstable one. Let's have a look 
at the run-times
~~~
/* The worst case scenario is of course is endless sorting as 
it randomizes the values of an array. 'n!' is the amount of
possible permutations of all the different values. */

Worst Case = O(n*n!);

/* Best case is only the amount of values, one needs to check
whether the array is sorted. This is of course only feasible
should it already be sorted*/

Best Case = O(n);
~~~
  
{% next "Specifications" %}

## Specification
As you might have noticed we have provided you with some starter code and some
complete functions for you to work with. In the following we will explain the functions
and specify what we want you to do.

{% next "int main(void)" %}
##int main(void)

***Note***: You do not need to write any code here.

The main function of the program initializes the integer array "A[]". Next
we also calculate the size of the array with our initialized integer "size".

After taking these steps we pass our array and its size into our actual sorting algorithm
specified through the function "stupidsort"

After the algorithm finished its work it will return a sorted array to your main
function. The main function then proceeds to pass in the sorted array "A[]" and "size"
into a printer function which prints out the array. 

{% next "void stupidsort(int A[], int size)" %}
##void stupidsort(int A[], int size)

This is where you need to start coding. The stupidsort function actually should only
check whether the array is sorted or not and then passing it into the actually sorting...or not ;)

Here you can incorporate the two functions "bool array_sorted(int A[], int size)" & 
"void randomize(int A[], int size)".

~~~
Pseudocode:

Check array is sorted;
    Sort array if needed;

~~~

{% next "bool array_sorted(int A[], int size)" %}
##bool array_sorted(int A[], int size)

This function should only look at the array and return a bool value.
~~~
Pseudocode:

Array is sorted;
    return True;
Array is not sorted;
    retun False;
~~~

{% next "void randomize(int A[], int size)" %}
##void randomize(int A[], int size)

This is where the magic happens. This is where the array gets randomized.
For this purpose there is actually a C function which we want you to use.
"**rand()**" this function is included in the **<stdlib.h>**. We encourage you 
to look at the specifications of this function online to understand its usage.

You can find documentation on this on W3Schools or GeeksForGeeks etc.

{% next "void pretty_printer(int A[], int size)" %}

You don't have to do anything here. We provide this function so that your array
can actually be printed out in the end. In the end if your program works
it should do this. 
~~~
Output = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
~~~

{% next "Libraries" %}

## Libraries
As you might have noticed we have written all of the required libraries for you into the header
of your program.

However, if you don't know which library contains what function, you find a plethora of documentation for
C libraries in the actual CS50 documentation, GeekForGeeks and W3Schools.

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/CAlgorithms/Stupidsort --local
~~~

**Have fun coding!**

