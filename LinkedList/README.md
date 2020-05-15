![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

## Complete linked_list.c

**Before tackling this task, make sure you have understood the concept of Linked Lists.
We recommend you watch this video in beforehand.**

{% video https://www.youtube.com/watch?v=zQI3FyWm144 %}

{% next %}

## Program Specifications

In order to solve this task you need to take care of **2 steps** in total. As you can see we have provided
you with some starter code! 

Your Task is to read in an Integer array and transfer it into a Singly Linked List. 
We have taken the liberty to already initialize your root/head for your Linked List. 
Your Task is to now write code into your main program which will add the remaining 9 integers included in your 
integer array 'A' to the linked list. You do not have to pay attention to any specific order. 
Just link the numbers one by one in the order they are stored in the array.

At the End of your main program you will notice that we have included a function called
'pretty_printer()'. This function will help you print out your linked list in our specified way.
There is no need to add or write any code for this function.

After your Linked List has been built and printed, it is time to get rid of it and free all the
memory you have allocated. In order to do so, we want you to use the 'free_ll()' function which we
have also predefined for you. This function should, when called upon, delete your Linked List
by freeing all the memory you have allocated. You can also do this recursively...however,
 you do not have to!;)

{% next "Library Talk" %}

## Libraries

**Note** that for this task we will only allow functions included in the "stdio.h" & "stdlib.h" libraries.
Therefore, try to rely on the basics C offers as well as your knowledge on pointers & structs to solve this task!

If you don't know which library contains which function, you can find a plethora of documentation for C libraries 
in the actual CS50 documentation or GeekForGeeks and W3Schools.

{% next "Output" %}

The output that will be printed to your terminal should look like the following
if successful:
~~~
Payload 1 = 3
Payload 2 = 200
Payload 3 = 30
Payload 4 = 20
Payload 5 = 49
Payload 6 = 34
Payload 7 = 60
Payload 8 = 1
Payload 9 = 9
Payload 10 = 10
~~~

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset4/LinkedList --local
~~~

**Have fun coding!**

{% spoiler "Hint" %}

## Pseudocode - Build Singly-Linked List
~~~
temp = root
for length of array
    node new
    new->payload = A[i]
    while temp->next != NULL
        temp = temp->next
    temp->next = new
    temp = new
~~~

{% spoiler "Hint" %}

## Pseudocode - Delete/Free Singly Linked List
~~~
trav = root                 # start at root/head.
while trav != null          # traverse to end of list.
    temp = trav             # save node pointer.
    trav = trav->next       # advance to next node.
    free temp               # free the saved one.
head = null                 # mark list to be empty.
~~~