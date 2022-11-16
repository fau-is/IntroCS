# Cinema

Imagine you run a small cinema in your backyard with just 16 seats (4 rows of 4 seats).
You have found a very inexpensive service provider on the Internet to handle the online reservations.
The only drawback: The service provider does not save the reservations with the corresponding row and seat number but with a consecutive number <= 15.
One hour before each movie you will receive two data sets from the service provider regarding the reservations, which are already sorted:
	- The consecutive numbers
	- The names of the visitors

Since you also want to accommodate spontaneous visitors without a reservation, you have installed a display at the gate to the street, which informs about free seats.
The display of the consecutive number like "Seat 13" is not very user-friendly with 4 rows of 4 chairs each.

{% next "Explanation %}

# Explanation

Your own information system, with which you operate the cinema, stores the seats not with consecutive numbers but with the help of a 4 x 4 matrix.
Each element of this matrix is a seat with typical characteristics of a cinema seat.
You have written a script for the automated transfer of the service provider data into your information system.
You can then feed the display with intuitive descriptions of row and seat numbers.

{% spoiler "Hints" %}
This text is initially hidden.
{% endspoiler %}