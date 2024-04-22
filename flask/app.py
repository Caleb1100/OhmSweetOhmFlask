from flask import Flask, send_from_directory, jsonify, render_template
from SensorData import sensorData

app = Flask(__name__)

# In-memory storage for device states
device_states = {
    "light": False,  # Initially off
    "awning": False
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sensor_data')
def sensor_data():
    # Use the imported function to get sensor data
    data = sensorData()
    return jsonify(data)

@app.route('/api/toggle_light', methods=['POST'])
def toggle_light():
    # Toggle the light state
    current_state = device_states["light"]
    new_state = not current_state
    device_states["light"] = new_state
    
    # Return the new state
    status = "on" if new_state else "off"
    print(f"Light toggled to {status}!")
    return jsonify({'status': status})

@app.route('/api/toggle_awning', methods=['POST'])
def toggle_awning():
    # Toggle the awning state
    current_state = device_states["awning"]
    new_state = not current_state
    device_states["awning"] = new_state
    
    # Return the new state
    status = "on" if new_state else "off"
    print(f"Awning toggled to {status}!")
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)