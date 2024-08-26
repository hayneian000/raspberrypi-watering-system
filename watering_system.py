import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request, jsonify
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Setup
GPIO.setmode(GPIO.BCM)

relay_pins = [18]

# Relay GPIO setup
for relay in relay_pins:
    GPIO.setup(relay, GPIO.OUT)
    GPIO.output(relay, GPIO.HIGH)

# Moisture sensor setup
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

sensor_1 = AnalogIn(ads, ADS.P0)

moisture_sensors = [sensor_1]

app = Flask(__name__)

def get_sensor_data():
    sensor_data = []
    for i, sensor in enumerate(moisture_sensors):
        sensor_data.append(round(sensor.voltage,4))
    return sensor_data
    
def check_moisture():
    status = []
    for i, sensor in enumerate(moisture_sensors):
        if sensor.voltage > 2.69: #if dry
            status.append(water_plant(i))
            print(f"Plant {i+1} is dry")
        else:
            status.append("Not watering")
            print(f"Plant {i+1} is moist.")
    return status
    
def water_plant(plant_id):
    GPIO.output(relay_pins[plant_id], GPIO.LOW)  # LOW IS ON 
    print(f"Watering plant {plant_id}...")
    status = "Watering"
    time.sleep(1)  # amount of time to water the plant
    GPIO.output(relay_pins[plant_id], GPIO.HIGH)  # turn pump off after watering
    return status

@app.route('/')
def index():
    status = check_moisture()
    sensor_data = get_sensor_data()
    return render_template('index.html', status=status, sensor_data=sensor_data, enumerate=enumerate)

@app.route('/manual/<int:plant_id>/<action>', methods=['POST'])
def manual_control(plant_id, action):
    if action == "on":
        GPIO.output(relay_pins[plant_id - 1], GPIO.LOW)  # LOW IS ON
        status = f"manually turned on"
    elif action == "off":
        GPIO.output(relay_pins[plant_id - 1], GPIO.HIGH)  # HIGH IS OFF
        status = f"manually turned off"
    elif action == "water":
        water_plant(plant_id - 1)
        status = "manually watered"
    else:
        status = "Invalid action"
    
    return jsonify({"status": status})

@app.route('/refresh/<int:plant_id>', methods=['POST'])
def refresh(plant_id):
    data = moisture_sensors[plant_id-1].voltage
    return jsonify({"data": round(data,4)})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
