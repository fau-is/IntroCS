![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

## Complete hashtable.c

**Before tackling this task, make sure you have understood the concept of Hashtables.
We recommend you watch this video in beforehand.**

{% video https://www.youtube.com/watch?v=nvzVHwrrub0&t=264s %}

{% next %}

## Program Specifications

In order to solve this task you need to take care of **4 steps** in total. As you can see we have provided
you with some starter code! 

Your Task is to read in a char *array and transfer it into a Hashtable. 
We have taken the liberty to already define the struct for this task called node. 
Your Task is to now write code into your main program which will add load
the 6 names of the Introduction to Computer Science staff into a Hashtable. 
You are required to solve this task by only using the methods we have predefined for you.

When the program is run 

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
temp = root                         # set equal to head/root.
for length of array                 # iterate over array.
    node new                        # create new node.
    new->payload = A[i]             # store payload.
    while temp->next != NULL        # check whether next exists.
        temp = temp->next           # if so go to end of list.
    temp->next = new                # store pointer new in temp next.
    temp = new                      # set temp to new for nex iteration.
~~~
{% endspoiler %}

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
{% endspoiler %}