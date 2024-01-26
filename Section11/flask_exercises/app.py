from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


"""
Specify flask app file and set debug model to true:
export FLASK_APP=app.py
export FLASK_DEBUG=1 
"""

#***************** Datetime ********************#
@app.route('/time')
def time():
    now = datetime.now(timezone('Europe/Berlin'))
    return "The current time in Berlin is {now}.".format(now=now)

""" 
With or without trailing slash at the end of url:

* end with "/" means folder, without means a file, many web browser automatically map to them to the same page.
* for some other protocols e.g. RESTful APIs with Django, the trailing slash matters.
* without /: allows relative URLs to continue working even if the trailing slash is omitted, consistent with how Apache and other servers work.
 Also, the URLs will stay unique, which helps search engines avoid indexing the same page twice. 
"""
#In case you want to ignore the trailing slash difference, but not recommended in real project.
#app.url_map.strict_slashes = False


    
#*********** Different routes for different users *************#

@app.route('/admin')
def greet_admin():
    return "hello admin!"

# pass user input from URI        
@app.route('/guest/<name>')
def greet_guest(name):
    return f"hello {name}!"


"""
python string format:
1. f-string: f"hell, {name}"
2. "hello, {name}".format()
"""

#******************* Type convert ***************************   

# What the error message says and how to fix it?
@app.route('/addOne/<num>')
def addOne(num):
    num += 1
    return num

# Why still not working? Read the error message
@app.route('/addOne/<num>')
def addOne(num):
    num = int(num)
    num += 1
    return num

# Solution: str -> int -> str
@app.route('/addOne/<int:num>')
def addOne(num):
    # num = int(num)  # uncomment this line if you don't want to and int: in the route
    num += 1
    return str(num)


# ***************** POST Request ********************

# simple POST request without having a html form
from flask import request
@app.route('/addOne', methods=["POST"])
def addOne():
    return str(int(request.form["number"]) + 1)

# command line tool "curl" to send http request, -x for http method (GET, POST, PUT, DELETE), -d for data
#curl -X POST -d "number=5" http://127.0.0.1:5000/addOne
    


# ************* Two routes sharing one function POST&GET*********
@app.route('/addOne/<int:num>', methods=["GET"])
@app.route('/addOne', methods=["POST"])
def addOne(num=None):
    if request.method == "GET":
        return str(num + 1)
    else:
        return str(int(request.form["number"]) + 1)


# ************ Two routes for login POST&GET ***************
@app.route("/login/<name>")
@app.route("/login", methods=["POST"])
def login(name=None):
    if request.method == "POST":
        name = request.form["name"] # Or: name = request.form.get("name")
        return "you are using POST method with {name}".format(name=name)
    else:
        return "you are using GET method with {name}".format(name=name)

"""
Note that request.form returns a python dictionary:
you can use both request.form.get("name") and request.form["name"] to retrieve values.
but get method allows to provide a default value if the key does not exist.
"""

# ************ One route POST&GET and html directly in python ***************
@app.route('/double', methods=['POST', 'GET'])
def double():
    if request.method == "POST":
        return str(int(request.form["number"]) * 2)
    else:
        return '''
        <form method="post">
            <input type=text name=number placeholder=number>
            <input type=submit name=double value=submit>
        </form>
        '''


# So far we only have one app.py file and can already create a basic website with simple functionalities. 
# Later we will see how to include html and css files to make flask project more structured and powerful.


# *************** Flask built-in methods **************
from flask import render_template, redirect, url_for ,session

# render_template 
@app.route('/')
def index():
    return render_template('index.html', name="Ana")

# redirect:
@app.route('/secret')
def secret():
    return redirect("/")

# url_for: return url for the defined function
@app.route("/login")
def login():
    return "This is the login Page"
print(url_for("login")) 

# session: store data across multiple requests made by the same client.
app.secret_key = "secret_key"
@app.route("/")
def index():
    session["counter"] = session.get("counter", 0) + 1
    return f"You have visited this page {session['counter']} times."



# ************** Add index.html file **************

# create form in templates/index.html
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return "User {name} successfully logged in!".format(name=username)
    else:
        return render_template('index.html')


# ************** Create multiplication table ***********
@app.route('/', methods=['POST', 'GET'])

def multi_table():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        return render_template('table.html', dim=request.form.get("size"))

"""
Pay attention to request.form.get("size"), the variable name is form.html name="size".
"""


# ************* Add css file *************

# Put css file in static folder, and link it to the html file you want, href is needed for flask to locate.
#<link rel="stylesheet" href="{{ url_for('static',filename='style.css') }}">