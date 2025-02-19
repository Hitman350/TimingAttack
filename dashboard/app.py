from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
import numpy as np
import os
import sys
import threading

# Add src directory to Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)

from aes import AES_Encryption                                                                                                                                                                                              # type: ignore
from timing_attack import TimingAttack                                                                                                                                                                                      # type: ignore

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode="eventlet")

attack_running = False  # Track attack state
attack_thread = None  # Store thread reference

@app.route("/")
def index():
    return render_template("index.html")

# Function to simulate timing attack and send real-time data
def generate_live_data():
    global attack_running
    attack_running = True

    key = os.urandom(16)
    aes = AES_Encryption(key)
    attacker = TimingAttack(aes)
    plaintext = b"Attack at dawn"

    for _ in range(500):
        if not attack_running:
            break  # Stop the attack loop when requested
        timing_value = attacker.perform_attack(plaintext)[0]
        socketio.emit("new_data", {"time": timing_value})
        eventlet.sleep(0.1)  # Simulate real-time updates

# Start Attack Stream
@socketio.on("start_stream")
def handle_start_stream():
    global attack_thread
    if not attack_running:
        attack_thread = threading.Thread(target=generate_live_data)
        attack_thread.start()

# Stop Attack Stream
@socketio.on("stop_stream")
def handle_stop_stream():
    global attack_running
    attack_running = False

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
