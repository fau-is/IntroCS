![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)

## Complete time.py

**Before tackling this task, make sure you have you have watched CS50s Lecture on python
and are comfortable with this new language.**

{% next %}

## Program Specifications

Time is precious and important. When it comes to working with dates and time in python things can get 
a bit complicated. However, this problem will help you understand working with time.

Your program should do the following. First we want you to print your local time including UTC 
(Coordinated Universal time) timezone information. You will notice that your "local" time might actually not correspond
to the time of the place in the world you are currently located in. Why is that?

After that we want you to print out the corresponding times in Europe/Berlin, 
America/New_York, Europe/London, Asia/Shanghai and Africa/Accra included in
list A.

Furthermore, every date and time needs to be printed out in the following specified way.
~~~
Datetime format:

Day/Month/Year, h:m:s
~~~

Your Output needs to look like the following (with the correct times and dates obviously):
~~~
Local : 01/06/2020, 12:16:21
Europe/Berlin : 01/06/2020, 14:16:21
America/New_York : 01/06/2020, 08:16:21
Europe/London : 01/06/2020, 13:16:21
Asia/Shanghai : 01/06/2020, 20:16:21
Africa/Accra : 01/06/2020, 12:16:21
~~~

{% next %}

Now in order to work with dates and times you will have to use the datetime library. You can find
comprehensive python docs via this [link](https://docs.python.org/3/library/datetime.html). The Library 
includes classes which allow you to manipulate dates and times. We recommend to read over this documentation
before tackling the task. Nevertheless, you can see a basic example of working with datetime below.
~~~
Example:

now = datetime.now()
print(now.time())
print(now.date())

Output:
15:45:34.996735
2020-06-15
~~~

Now additionally when working with different timezones there is an helpful open source module called
Python pytz (python timezone). Essentially this module is very useful when working with timezone definitions as
well as calculating times in relation to different timezones. This module allows you to do the following.

~~~
Example:

#Try out this line of code in your IDE ;)
print(pytz.all_timezones)
~~~

There is some great open source explanations on working with the pytz module from [JournalDev](https://www.journaldev.com/23370/python-pytz).

{% next "Library Talk" %}

## Libraries

**Note** that for this task we will only allow methods included in the datetime library and pytz module.

If you don't know which library contains which function, you can find a plethora of documentation for python libraries 
in the actual python docs or the CS50 documentation, GeekForGeeks and W3Schools.

{% next "Check & Submit" %}

## Check 

You can check your code using the following check50 command:

~~~
check50 fau-is/IntroCS/Pset6/Time --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset6/Time
~~~
