![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

## Complete tries.c

**Before tackling this task, make sure you have understood the concept of Tries.
We recommend you watch this video in beforehand.**

{% video https://www.youtube.com/watch?v=MC-iQHFdEDI&t=828s %}

{% next %}

## Program Specifications

In order to solve this task you should follow the specifications closely. 
This task requires some time. 
However, after completing this exercise you understand the concept of Tries.

The overall task comprises reading in the names of 7 cities from cities.txt into the trie. 
Then you compare the names of the cities to the names you have stored in the
Trie to see whether your Trie loaded correctly. 
Finally, you conclude the task by unloading the Trie, i.e. freeing allocated memory.

Nevertheless, to complete this exercise you will first have to write some code that reads in the cities from 
cities.txt into a string array. 
We use this string array to check whether you loaded your Trie correctly.

You should work on the given functions in the following order.
~~~
1.  int main(void)
2.  unsigned int counting(node *temp) 
3.  bool check(const char *word)
4.  unload()
~~~

**Have fun coding!**

{% next "int main(void)" %}

## int main(void)

**The main function includes your Trie load.**

Let's go through the main function step by step. 
First, you initialize a string and assign the file name "cities.txt" to it.
Hence, you can create a FILE pointer to let your program interact with the file. 

The next step is to initialize the Trie's root node. 
If you scroll to the top of your program you notice that there is a struct Node.
~~~C
typedef struct node
{
    bool is_city;
    struct node *children[N];
}
node;

node *root;
~~~

The properties of your struct are a bool named _is\_city_, and the node array pointer _children_. 
The bool is\_city, if set to true, indicates that the word is a city name. 
Children, the node pointer array, stores pointers to other nodes. 
This allows you to navigate through your Trie. 
To access properties in a struct, use the following syntax.
You should already be familiar with it from the CS50 lectures.:
~~~C
node *root
node *temp;

root -> is_city = false;
root -> children[0] = temp;
~~~

Now we have initialized our root node. 
Next, we need to allocate some memory to store our root node. 
We do this by using the function _malloc()_. 
We did this for you already. 
By convention in C you must check whether the memory allocation was successful. 
You do this by checking whether the struct you created is not equal to NULL. 
If the struct is NULL, the operating system denied your memory allocation.
In this case, you should return false or return 1. 
Again, we did this for you already. 

The next step is to set the bool property of your root node to the right value.
In our case, we set it too false.  
Since we do not want to add a city name which is an empty string ("") to our Trie. 
Finally, we must ensure that "children[N]" does not contain any values from previous program usage. 
Therefore, we use a loop to iterate over "children[N]" and set the values at every index to NULL.
We are finished setting up the basis for our trie.

Let's continue with prerequisites for file reading. 
First, we initialize a file pointer "file" and open our file "cities.txt". 
Second, we, again, check whether opening the file was successful.
If the file pointer remains NULL, we could not open the file. 
In this case, by specification we call the unload()-function and return false.

We are now done with the prerequisites, let's dive into the basic trie functionalities now.

{% next "load in main" %}
## The Load

This is where it actually gets interesting!
Now it is your time to shine! 
You shall load your trie data-structure. 
We initialized a string buffer called "word" for you.  
Use it throughout the load operation. 
The task at hand is to iterate through the cities.txt file, 
and load every word into the trie. 
Therefore, we use a while-loop to iterate through "cities.txt".
We fetch the city names separated by line breaks ('\n') from the file one by one.

Look at this Pseudo Code shortly.
We will drill down each of the steps below.
For each city name we: 
1. Store it in the buffer "word"
1. Check its length
1. Create a new node pointer current which points to root
1. Loop over the characters in word:
    1. Get the alphabetical index of the character
    1. If current->children[alphabetical index] is NULL:
        1. Set current to current->children[alphabetical index]
    1. Else:
        1. Create new node
        1. Assign the new node to current->children[alphabetical index]
        1. Set current to current->children[alphabetical index]
1. Set current's is\_city to true

After storing the city name in "word", you find out the length of the word at hand. 
You can use the strlen() function from the string.h library.

Go on and create a node pointer and set it to your root node 
so that you don't endanger your valuable root node. 
Remember with data structures it is all about knowing where to start when 
searching within them. 
Therefore, you should never directly manipulate your head or root to minimize the risks. 
Creating a temporary node pointer current does the job for you:
~~~C
node *current = root;
~~~
The next step is to create a loop which iterates over your word to access each 
character. 
Thereafter, you map it to its corresponding place in the children array of the corresponding node of the Trie.
You must unify your characters as some might be uppercase and others might be lowercase. 
You can use the tolower() function included in the ctype.h library. 
Using this function on lowercase characters won't change anything, they will remain lowercase ;). 
You will need to figure out how to actually map each character to it's corresponding place in the node pointer arrays. 
As a refresher if you have the word "Anagram", the first letter of your word should be stored at index 0 in the array as 'A' or 'a' is the
first letter in the Alphabet. 

Remember that lowercase 'a' is at place 97 in the ascii table. 
~~~C
'a' - 97 = 0; // just saying ;)
~~~
Great, now we have taken care of finding the index where we want to store our pointer to the next node
that will in return store the pointer for the next letter and so on...we actually have to take care of that.
In order to do so we first need to find out whether our current node already has a pointer stored within its
children[N] property at the index we just calculated. A simple 'if' condition should suffice!

If there is indeed nothing stored at that index we have to first create a new node that we can store at said place!
so we'll to that! Don't forget to check whether you have actually allocated memory as discussed earlier ;).
After you have created your new node you will have to store it at the index within your children array of your 
current node. Great! Don't forget we are within a Loop therefore we have to update our current node! In the next
iteration our current node should be the new node we have just created. 

Nevertheless, what happens if there already is a pointer stored in our current node at the calculated index?
Well, in that case we just have to update our current node to the next node in order to follow the path untill the 
letter we want to store has not been initialized! Loop Magic!

The last step for you load before you load your next word should obviously be to set the bool is_city
in the final node you have created to 'true' to indicate that the word is indeed a city!

That's all for the Load Folks!

{% next "unsigned int counting(node *temp)" %}

## unsigned int counting(node *temp)

**This method counts the number of cities loaded into your trie**

Now this can be done iteratively...However, to quote Doug Lloyd "Recursive Code is sexy."
So that's what we're going to do!

## Counting Cities

Now we could obviously introduce a global variable (which we have) and increment it every time we load
a city into our Trie but where is the fun in that?

As you can see in the main function we initialize a node 'temp' and set it equal to the root node
which we pass into our counting method. 

The first step within our counting method is to check what value our _is_city_ bool has. 
If it is equal to _true_ well then we have to increment our 'count' (which we have conveniently declared globally).
The next step is to iterate through _children_ property within the temp node and if there is a pointer
stored at the current index we pass the node correspondent to that pointer into the counting method once again.
From the prior sentence the base case should be pretty clear as well as where recursion actually comes into play!

Lastly if the base case is not fulfilled, and you 'break out of the cycle' we just have to return the count.

That's all there is to it really :)

Pseudo Code:
1. Check if temp->is_city is true
    1. increment count
1. Iterate through children for N times
    1. Check if temp->children is not NULL
        1. pass temp->children into counting method
1. Return count
 

![archer-recursion](https://i.imgur.com/ojcxhyQ.png)

{% next "bool check(const char *word)" %}

## Checking for cities

**This method checks whether your Trie has loaded all the cities**

The string array 'A', has all the cities included and therefore, this is what is checked against.

The function returns a bool. If the city exists within the Trie it returns true if not it returns false.
In order to walk trough the Trie we require a temporary node which initially is set to equal root.

After that a loop is required to iterate for the length of the string being checked against. 
Just as in the Load a simple For-Loop suffices. 

Moving on we have to calculate the index the same way we did in the load function for the city you are checking.
Don't forget that we only want to check the word as long as the string we are checking against doesn't end i.e.
we do not want to check for the '\0' character. A simple if condition for this purpose will do the trick.

Now the first thing we check is whether a value exists at the index within _children_ of our temp
node. If not we have to return false as our word doesn't exist. However, if there is a value we have to 
move our temp node to the next node to check whether at the corresponding index of the next letter a pointer to a
subsequent node is stored...and so on. The final check, as soon as the loop finishes iterating through the string we're
checking against is whether the value of the _is_city_ property is _true_. If so we return true otherwise it goes 
without saying we need to return false.

This concludes the check function().

Pseudocode:
1. create temp node and set to root
1. iterate through string you check against
    1. index the letters of the string
    1. if the letter of the string is not "\0"
        1. check if children at that index is NULL
            1. return false
        1. set temp = temp->children
1. if temp->is_city is true
    1. return true
1. else
    1. return false   
      
{% next "unload()" %}

## Unloading your Trie

**This function unloads your Trie by freeing all the allocated memory**

Now this function will again be implemented recursively. You can also do it iteratively!

A temp node will be set to root in order to be able to walk through the Trie.
In order to free all the allocated memory we need to find all the nodes within the 
Trie. 
So the essence of the unload function is to iterate through the _children_ property of the 
temp node. If at any given index there is a node pointer stored we have to pass that 
node into the unload function once again. As soon as the base case is not fulfilled any more
and your loop finishes we have to use the free() command on the temp node. 
This will free all the allocated memory and successfully unload the Trie.

That's all there is to the unload function.

Pseudo Code:
1. iterate over temp->children
    1. if temp->children is not NULL
        1. pass temp->children into unload function
1. free temp


{% next "Debrief" %}

## Debrief

If you followed all the steps you should now have implemented a Trie successfully! Congratulations.

Please submit your code to us so that if any issues arise we can help you accordingly!

## Submit

You can submit your code to us via the following submit50 command:

~~~
$submit50 fau-is/introcs/Pset4/Trie
~~~

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset4/Trie --local
~~~
