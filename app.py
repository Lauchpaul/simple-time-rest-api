from flask import Flask, jsonify 
from datetime import datetime

"""
from flask import Flask, jsonify 

We import from the flask module (A module is basically a Python file) the Flask class...
We also import the function jsonify. It's useful for converting Python objects into JSON format.

from datetime import datetime

We import the class datetime from the datetime module. It's used to get the current date and time.

*Note: Classes are usally written starting with a capital letter: "Flask" but sometimes they can start
with a lowercase letter: "datetime"


"""

app = Flask(__name__) 
"""
 Here we create a new Object using the class "Flask" we give it the attribute __name__
 __name__ is a special variable that holds the name of the current module.
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

if __name__ == '__main__':
    # host='0.0.0.0' is crucial to make the app accessible from outside the container
    app.run(host='0.0.0.0', port=5000)

