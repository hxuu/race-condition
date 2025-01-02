from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

BAN_FILE = './condition.ban'

@app.route('/')
def handle_request():
    now = time.time()

    # Read ban time
    if os.path.exists(BAN_FILE):
        with open(BAN_FILE, 'r') as f:
            ban_time = float(f.read())
    else:
        ban_time = 0.0

    response = {"start": now}

    if now <= ban_time:
        response["message"] = "you're banned"
        return jsonify(response), 403

    # Simulate processing delay (100ms)
    time.sleep(0.1)

    # Write new ban time
    with open(BAN_FILE, 'w') as f:
        f.write(str(now + 60))  # Ban for 1 minute

    response["message"] = "success"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

