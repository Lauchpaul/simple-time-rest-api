"""
Hello, this is a simple example of a REST API.
 
I used this project to learn about many things like:

- OOP
- Imports/Modules in Python
- Decorators in Python
- __main__ and its meaning

I commented almost every line of the code, so you can understand my learnings :)

I hope if someone reads it, they find it helpful for their Python journey.
"""


from flask import Flask, jsonify 

from datetime import datetime

"""
from flask import Flask, jsonify 

We import from the flask module (A module is basically a Python file) the Flask class...
We also import the function jsonify. It's useful for converting Python objects into JSON format.

from datetime import datetime

We import the class datetime from the datetime module. It's used to get the current date and time.

*Note: Classes are usually written starting with a capital letter: "Flask" but sometimes they can start
with a lowercase letter: "datetime" f*cking python devs don't even use their own naming conventions ;)


"""

app = Flask(__name__) 
"""
 Here we create a new Object using the class "Flask" we give it the attribute __name__
 __name__ is a special variable that holds the name of the current module. (A module is another Python file!)
 In this case it's set to '__main__' because we are running the script directly. When it's imported in another
 script it will have the name of the module.
 As an example if I import file2 into file1, inside file2 
 "__name__" will have the value "file2".
"""



@app.route('/time', methods=['GET'])
def get_time():
    # Fetch current server time
    now = datetime.now()
    # Return a structured JSON response
    return jsonify({
        "status": "success",
        "server_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "UTC" if now.tzinfo is None else str(now.tzinfo)
    })

"""
The @app.route decorator connects this Python function to a specific URL path
on the Flask web server. In this case, the function is linked to '/time'.

The methods=['GET'] argument defines which HTTP methods are allowed.
Here, only GET requests are accepted. A GET request is typically used
when a client wants to retrieve information from the server.

Internally, Flask stores a mapping between the URL path ('/time')
and the Python function get_time(). You can imagine it conceptually
like this:

if request.path == "/time":
    return get_time()

When a client (for example a browser, curl, Postman, or another application)
sends a GET request to '/time', Flask automatically detects the matching route
and executes the get_time() function.

The return value of get_time() is then converted into an HTTP response
and sent back to the client.

jsonify() is used to convert the Python dictionary into valid JSON format
while also setting the correct HTTP Content-Type header automatically.

This mechanism is one of the core concepts of Flask:
URLs are mapped to Python functions using decorators.

The Decorator basically "adds" the function get_time() to the method app.route, so we can retrieve the output
of the function get_time() when we make a request to '/time' in a browser or curl yk????
"""


if __name__ == '__main__':
    # host='0.0.0.0' is crucial to make the app accessible from outside the container
    app.run(host='0.0.0.0', port=5000)