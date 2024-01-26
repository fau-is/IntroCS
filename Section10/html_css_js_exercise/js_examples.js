// conditions
let x = 1;
let y = 2;
let z;

if (x==y){
  z = true;
    }
else {
  z = false;
}

alert(z)

// ?: expression
z = x==y ? true : false


// switch
let i = 1;

switch (i) {
  case 1:
    alert("you entered 1");
    break;
  case 2:
    alert("you entered 2");
    break;
  case 3:
    alert("you entered 3");
    break;
}


// Loop: factorial: 4! = 4*3*2*1

let factor = 1;
for (let i = 1; i <=4; i++) {
    factor *= i;
}
console.log(factor);

for (let i=5; i>=1; i--) {
    factor *= i;
}
alert(factor);


// Oject properties and methods
let herbie = {
  year: "1963",
  model: "Beetle",
  sound: "honk.mp3",
  honk: function(){
    alert("Honk from " + this.sound);
  }
};

herbie.honk();


// get the value of each property
for (let prop in herbie) {
alert(herbie[prop]);
}


// Array operations
let weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

// for in
for (let day in weekDays) {
    console.log(day);
}

// for of
for (let day of weekDays) {
    console.log(day);
}

// concantenate string & number
for (let day in weekDays) {
  alert( weekDays[day] + " is the number " + (day +1) +" day of the week!");
}


// array property and methods
weekDays.length;
weekDays.pop(); // remove last element and return the element
weekDays.push(1); // add element to the end and return new array length
weekDays.shift(); // remove first element from array and return the value
weekDays.map(); //call function on each element and return the new array



// event handlers with onclick
<button id="greeting"> Greeting </button>
<button id="color"> Color </button>
<button id="time"> Time </button>


document.getElementById("greeting").onclick = function() {
  alert("Hi!");
 }

document.getElementById('color').onclick = function(){
  document.getElementById('color').style.backgroundColor = 'green';}


document.getElementById('time').onclick = function() {
    document.getElementById('time').innerHTML = Date()}


// Event handlers with addEventListener

<button id="red"> Red </button>
<button id="green"> Green </button>
<button id="blue"> Blue</button>

let body = document.getElementById('body');
document.getElementById('red').addEventListener('click',function() {body.style.backgroundColor='red';});
document.getElementById('green').addEventListener('click', function(){body.style.backgroundColor='green';});
document.getElementById('blue').addEventListener('click', function(){body.style.backgroundColor='blue';});



// jquery include in the head
<script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

//jquery event click
document.getElementById('greeting').onclick = function () {
    alert("hi");
 }

$("#greeting").click(function() {
  alert("Hi from jQuery!");
})

// jquery change color
$('#myh').css('background-color', 'green');
document.getElementById('myh').style.backgroundColor = 'green';
