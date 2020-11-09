![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete inverse.c
Write a program that takes a command line input only allowing 1 Word. 
If a  user inputs 2 words into the command line your program should automatically exit  with the correct exit code i.e. return 1;
Make sure that the input only consists of letters in the alphabet. 

Your main function should only take in the command line argument and invert the string. Use a separate function 
to check whether or not your string only contains letters of the alphabet before doing the actual inverting. We have
initialized a function you can use already called alphabet(). In the end your main program
should print out the inverted string.

~~~
Input = "Hello"; 
Output = "olleH";

Input = "H1llo";
Output = "Input word";
~~~

You only require the libraries already given in the header. If unsure what functions
are included in these libraries and how they work you can find a Plethora of documentation for C libraries 
in the actual CS50 documentation or GeekForGeeks & W3Schools.

We have included some basic checks for you to see whether your program works in the intended way.
You can run this command in your Terminal to run the check
~~~
$check50 fau-is/IntroCS/Pset2/Inverse --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset2/Inverse
~~~

{% spoiler "Hints" %}
HINT: Use isalpha() in order to check for letters of the alphabet
{% endspoiler %}
