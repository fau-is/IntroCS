![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

## Complete tries.c

**Before tackling this task, make sure you have understood the concept of Tries.
We recommend you watch this video in beforehand.**

{% video https://www.youtube.com/watch?v=MC-iQHFdEDI&t=828s %}

{% next %}

## Program Specifications

In order to solve this task you will have to follow each specification step closely. This task
requires some time. However, after completing this exercise you will have understood Tries.

The main task consists of reading in the names of 7 cities from the cities.txt file into the trie data 
structure you will create. Then you will compare the names of the cities to the names you have stored in your
Trie in order to see whether you have loaded your Trie correctly. Finally, you will conclude this exercise by unloading
your Trie i.e. freeing the allocated memory.

Nevertheless, to complete this exercise you will first have to write some code that will read in the cities from 
cities.txt into a string array. This string array will then be used to check whether you have loaded your Trie correctly.

When working on this task you should work on the already given functions in this order.
~~~
1.  int main(void)
2.  unsigned int counting(node *temp) 
3.  bool check(const char *word)
4.  unload() // this function will unload your Trie by freeing all the allocated memory
~~~

**Have fun coding!**

{% next "int main(void)" %}

## int main(void)

**The main function will include your Trie load.**

Let's go through the main function step by step. First you initialize a string
and give it the name of your .txt file in order to be able to assign this value
to a FILE pointer to work with it throughout your program. 

The next step ist to initialize your root node. If you scroll to the top of your program 
you will notice that there is already a struct defined named Node.
~~~
typedef struct node
{
    bool is_city;
    struct node *children[N];
}
node;

node *root;
~~~
The Properties of your struct are for one a bool named is_city which, if set to true will indicate
that the word loaded into a trie is indeed a city. Further, the structs contains a property called
children. This is a node pointer array, meaning the array children[N] can store pointers to other
nodes. This allows you to navigate the paths of your Trie. In order to access properties in a struct 
you can use the following syntax which you should already be familiar with.:
~~~
node *root
node *temp;

root -> is_city = false;
root -> children[0] = temp;
~~~

Now we have already initialized our root node. However, we also need to allocate memory in order to 
store our root. We do this by using the function malloc(). As you can see we have also already done this
for you. By Convention in C you are required to check whether you have actually allocated memory. You do this 
by checking whether the struct you have created and allocated memory to equals NULL. If this is the case
there has been no memory allocated, and you should return false or return 1. Again we have already
taken care of this for you. 

The next step is to set the bool property of your root node to the right value.
Now in our case this would be false as we do not want to indicate a city within our root node. Finally,
we need to make sure the node pointer array "children[N]" does not contain any values as we have not loaded
anything yet. Therefore, we use a simple For-Loop to iterate through the array and set the values at every index 
equal to NULL.

Continuing with our code we now initialize a file pointer "file" and open our file cities. Again we 
check whether our file is empty and if so by convention we call our unload() function and return false.

## The Load

This is where it actually gets interesting! Now it is your time to shine! You are required to 
build i.e. load your trie data-structure. We have initialized a string buffer called "word" which we 
will use throughout the load operation. The task at hand is to iterate through the cities.txt file
and insert every word into the trie. Therefore, we use the While-Loop to iterate through our file fetching
the string stored in each line and storing it in our buffer 'word' to use it in our program.

Now the first thing you will have to do is to find out the length of the word at hand. You can use
the simple strlen() function included in the string.h library.

You should now go on and create a node and set it equal to your root node so that you don't run into the
danger of loosing your root node. Remember with data structures it is all about knowing where to start when 
searching within them. Therefore, you should never directly manipulate your head or root in order to minimize the
risk. Example.:
~~~
node *current = root;
~~~
Moving on, the next step is to create a loop which will iterate over you word in order to access each 
character and map it to its corresponding place in the array property of every node that will be created.
Obviously you need to unify your characters as some might be uppercase and others might be lowercase. In order
to do this you can use the tolower() function included in the ctype.h header. Using this function on lowercase
characters won't change anything, they will remain lowercase ;). You will need to figure out how to actually 
map each character to it's corresponding place in the node pointer arrays. As a refresher if you have the
word "Anagram" the first letter of your word should be stored at index 0 in the array as 'A' or 'a' is the
first letter in the Alphabet. Remember that lowercase 'a' is at place 97 in the ascii table. 
~~~
'a' - 97 = 0; // just saying ;)
~~~
Great now we have taken care of finding the index where we want to store our pointer to the next node
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

**This function will count the number of cities loaded into your trie**

Now this can be done iteratively...However, to quote Doug Lloyd "Recursive Code is sexy."
So that's what we're going to do!

## Counting Cities

Now we could obviously introduce a global variable (which we have) and increment it every time we have loaded
a city into our Trie but where is the fun in that?

As you can see in the main function we have initialized a node 'temp' and set it equal to the root node
which we pass into our counting function. 

The first step within our counting function should be to check what value our is_city bool has. 
If it is equal to true well then we will have to increment our 'count' (which we have conveniently declared globally).
The next step would be to iterate through the children[N] property within your temp node and if there is a pointer
stored at your current index you should pass the node correspondent to that pointer into your counting function once again.
From the prior sentence the base case should be pretty clear as well as where recursion actually comes into play here!

Lastly if your base case is not fulfilled, and you 'break out of the cycle' you will just have to return your count.

That's all there is to it really :)

![fau-logo](https://i.imgur.com/ojcxhyQ.png)

{% next "bool check(const char *word)" %}

## Checking for cities

**This function will check whether your Trie has loaded all the cities**

The string array 'A', if implemented correctly, has all the cities included and therefore, this is what we will check against.

The function returns a bool. If the city exists within your Trie it will return true if not it will return false.
Again in order to walk trough your Trie we require a temporary node which initially will again be set to equal root.

After that we require a loop for the length of the city we want to check against. Just as in the Load a simple For-Loop 
should suffice. 

Moving on you will have to again calculate the index the same way you did in the load function for the city you are checking.
Don't forget that you only want to check the word as long as the string you are checking against didn't end i.e.
you do not want to check for the '\0' character. A simple if condition for this purpose will do the trick.

Now the first thing you should check is whether a value exists at the index within the children[N] array of your temp
node. If not then you will have to return false as your word doesn't exist. However, if there is a value you will have to 
move your temp node to the next node to again check whether at the corresponding index of the next letter a pointer to a
subsequent node is store...and so on. Your final check as soon as you have finished looping through the city you're checking
against is whether the value of the bool property is 'true'. If so return true otherwise it goes without saying you should 
return false.

This concludes your check function().

{% next "unload()" %}

## Unloading your Trie

**This function will unload your Trie by freeing all the allocated memory**

Now this function will again be implemented recursively. You can do it iteratively!

Again your temp node will be set to root in order to be able to walk through your Trie.
In order to free all the allocated memory you will have to find all the nodes within the 
Trie. 
So the essence of your unload function is to iterate through the children property of your 
temp node. If at any given index there is a node pointer stored you will have to pass that 
node into your unload function once again. As soon as your base case is broken and your loop finishes
you will have to use the free() command on your temp node. This will free all the allocated memory and successfully unload
your Trie.

That's all there is to the unload function.

{% next "Debrief" %}

## Debrief

If you have followed all the steps you should now have implemented your own Trie successfully! Congratulations.

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
