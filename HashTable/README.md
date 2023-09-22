---
files: [hashtable.c]
window: [terminal]
---
![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)

## Complete hashtable.c

**Before tackling this task, make sure you have understood the concept of Hashtables.
We recommend you watch this video in beforehand.**

{% video https://www.youtube.com/watch?v=nvzVHwrrub0&t=264s %}

{% next %}

## Program Specifications

In order to solve this task you need to take care of **4 steps** in total. As you can see we have provided
you with some starter code! 

~~~
1. int main(void) // the main programm will largely consist of the loading
2. int hash(char *name) // this is your hashfunction
3. bool search(char*to_search, node *hashtable[]) // this function will search for given input
4. void unload_ht(node *head) // this function will free allocated memory
~~~

Your Task is to read in a char *array and transfer it into a Hashtable. In order
to do this successfully you will have to write a hash function. You can find more information on
hash functions below. 
We have taken the liberty to already define the struct for this task called node. 
Your Task is to now write code into your main program which will add load
the 6 names of the Introduction to Computer Science staff into a Hashtable. 
You are required to solve this task by only using the methods we have predefined for you.

When the program is run we have written some code which will pass in 2 strings into the
search function one of which exists within the provided array.
~~~
Output: Chris exists;
Output: Tobias does not exist;
~~~

Finally the hashtable will be unloaded via the unload function.

{% next "Hash functions" %}

CS50s course material touches hash functions as well as their areas of application briefly.
Nevertheless, a hashtable is the best coding task in order to come up and practice implementing
your own hash function.

In short a hash function is a mathematical function that converts an input value into a fix sized
numeric value. The values that are being returned by any hash function are called hash values. 
~~~
Example:

Input = Cello;
Output = 143;
Input = Rudolph
Output = 167
~~~

Hash functions are used with hash tables naturally. Generally the usage of a hash function constitutes a
rope-walk in-between search times and storage space. Writing an efficient hash function can therefore, 
be an entire science of its own. 

In this exercise there is no specification how your hash function should look like. You are totally free
to execute anything you might deem sensible.

**The only specification is that the hash value needs to be between 0-9 inclusively**

{% spoiler "Hint" %}

The Modulo operator is always helpful here!
 
{% endspoiler %}


{% next "Library Talk" %}

## Libraries

**Note** that for this task we will only allow functions included in the "stdio.h", "stdlib.h", "string.h" & "stdbool.h" 
libraries. Therefore, try to rely on the basics C offers as well as your knowledge on pointers & structs 
to solve this task!

If you don't know which library contains which function, you can find a plethora of documentation for C libraries 
in the actual CS50 documentation or GeekForGeeks and W3Schools.

{% next "Check & Submit" %}

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset4/HashTable --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset4/HashTable
~~~

**Have fun coding!**
