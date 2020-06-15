![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)

## Complete time.py

**Before tackling this task, make sure you have you have watched CS50s Lecture on python
and are comfortable with this new language**

{% next %}

## Program Specifications

Time is precious and important. When it comes to working with dates and time in python things can get 
a bit complicated. However, this problem will help you understand working with time.

Your program should do the following. First we want you to print your local time in UTC 
(Coordinated Universal time). You will notice that your "local" time might actually not correspond
with the time of the place in the world you are currently located in. 

After that we want you to print out the corresponding times in Europe/Berlin, 
America/New_York, Europe/London, Asia/Shanghai and Africa/Accra provided in
list A.

Furthermore, we want that every date and time is printed in the following specified way.
~~~
Datetime format:

Day/Month/Year, h:m:s
~~~

Your Output needs to look like the following (with the correct times and dates obviously):
~~~
Local: 01/06/2020, 12:16:21
Europe/Berlin : 01/06/2020, 14:16:21
America/New_York : 01/06/2020, 08:16:21
Europe/London : 01/06/2020, 13:16:21
Asia/Shanghai : 01/06/2020, 20:16:21
Africa/Accra : 01/06/2020, 12:16:21
~~~

{% next "" %}

Now in order to work with dates and times 

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
