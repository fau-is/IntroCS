![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

## Complete clean.py

**Before tackling this task, make sure you have you have watched CS50s Lecture on python
and are comfortable with this new language**

{% next %}

## Program Specifications

Your task is to help a teacher. For an exam this teacher wants to test students knowledge
of poems by certifying whether they know the exact syntax and punctuation of each poem. As
getting rid of punctuation, special signs etc. in poems is a tedious task the teacher now needs 
a program that will automate this process. 

In order to test your program we have provided you with a poem silent_sea.txt. Have a look at the file, you
will recognize the poem has a lot of punctuation and special signs such as "!", ",", ";", "-" etc.

Your target is to write a program that will, literally speaking, clean the poem from punctuation and
special signs as given above. In order to do so your program is required to read in the poem, clean it
and write it into a new file, here specified by silent_sea_clean.txt.

Your output file should include the poem looking like this.:
~~~
How Soft The Shades of Evening Creep

How soft the shades of evening creep
Oer yonder dewy lea
Where balmy winds have lulled to sleep
The tenents of the tree

No wandring breeze is here to sweep
In winding ripple oer the deep
Yet swells the evening sea

How calm the sky Rest ocean rest
From storm and ruffle free
Calm as the image on thy breast
Of her that governs thee
And yet beneath the moons mild reign
Thy broad breast heaves as one in pain
Thou dark and silent sea
~~~

{% next %}

Cleaning text is a common task that has to be done in coding. Now in order to do so 
python's string library offers a couple of functionalities that will definitely come in useful 
when tackling this issue. Have a look at the [python - Docs](https://docs.python.org/3/library/string.html) for the
string library.

**Your output file must not include any signs included in .punctuation of the string library.**

Furthermore, we recommend that you use the **.append** method inherent to python as you will most likely have to 
work with Lists in order to tackle this problem. 
~~~
Example: 

A = ("IntroCS", "is")
string = "fun"
A.append(string)
print("A =", A)

Output:

A = ('IntroCS', 'is', 'fun')
~~~

Additionally, you will most definitely require the **.join** method which allows you to concatenate separate items to a string.
~~~
Example: 

A = ("IntroCS", "is", "fun")
string = " ".join(A)
print(string)

Output:

"IntroCS is fun"
~~~

**Have fun coding!**

{% next "Library Talk" %}

## Libraries

**Note** that for this task we will only allow functions included in the string 
library Therefore, try to rely on the basics python offers

If you don't know which library contains which function, you can find a plethora of documentation for python libraries 
in the actual python docs or the CS50 documentation, GeekForGeeks and W3Schools.

{% next "Check & Submit" %}

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset6/Clean --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset6/Clean
~~~

{% spoiler "Hint" %}

First you need to read your file into a string. Further, you will have to initialize a list.
Then you go through your string character for character to check for any punctuation. If you find punctuation you do 
not append anything. Vice versa if your character is not included in .punctuation you just append the character to 
a normal list. Finally, you concatenate your list to a single string which you then write into your 
Output file.
 
{% endspoiler %}
