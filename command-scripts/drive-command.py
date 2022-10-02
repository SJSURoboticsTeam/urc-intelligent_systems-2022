import sys
import requests
import serial.tools.list_ports as port_list
sys.path.append( '../modules/Serial')
from Serial import SerialSystem
import json
import time

port = "/dev/ttyUSB0"
example_json = '{"heartbeat_count":0,"is_operational":1,"wheel_orientation":0,"drive_mode":"D","speed":0,"angle":0}'


get_initial_commands_url = "http://192.168.50.243:5000/drive"

web_response = requests.get(get_initial_commands_url)
print("Getting data from: " + web_response.text)

try:
    serial = SerialSystem(port, 38400)
    print("Using port: " + port)
except:
    ports = list(port_list.comports())
    print('====> Designated Port not found. Using Port:', ports[0].device)
    port = ports[0].device
    serial = SerialSystem(port, 38400)

homing_end = "Starting control loop..."
status = ''
while True:
    response = serial.read_serial()
    if homing_end in response:
        print("Parsing Data from Pi...")
        while True:
            serial.write_serial(web_response.text)
            response = serial.read_serial()
            time.sleep(1)
            json_format = json.loads(example_json)
            #json_format = json.loads(response)

            web_response = requests.get(get_initial_commands_url, params=json_format)

