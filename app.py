from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

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
