import socket
import json
from opcua import Server
import datetime
import random
import time


def RequestData(sensor):
    message = "request"
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    if data:
        jsonData = json.loads(data)

        for datas in jsonData:
            for sensorname in sensor: # sensor name in the setting

                if datas['name'] == sensorname:
                    globals()['Sensor_{}'.format(sensorname)] = float(datas['value'])
                    globals()[datas['name']].set_value(globals()['Sensor_{}'.format(sensorname)])

                    break
    else:
        time.sleep(0.5)

HOST = '127.0.0.1'
PORT =  8192

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# until it the has success reconnected in the socket
connected = False
while not connected:
    try:
        client_socket.connect((HOST, PORT))
        connected = True
        print("connected OK")
    except socket.error:
        print("excpetion error")
        time.sleep(2)


sensor = []

message = "setting"
client_socket.sendall(message.encode())
data = client_socket.recv(8192)
if data:
    

# setting message sand
    
    jsonData = json.loads(data)
    num = 0
    json_len = len(jsonData)
    for val in jsonData:
        if num == 0:
            opcip = val['ip']
            server = Server()

            url = "opc.tcp://"+opcip+":4840"
            server.set_endpoint(url)

            name = "OPCUA_SIMULATION_SERVER"
            addspace = server.register_namespace(name)

            node = server.get_objects_node()

            # setting message sand
            Param = node.add_object(addspace, "Paramters")   
            for value in jsonData:
                num = num+1
                if num > 1:
                    print(value['name'])
                    globals()[value['name']] = Param.add_variable(addspace, "Sensor_{}".format(value['name']),0)
                    globals()[value['name']].set_writable()
                    sensor.append(value['name'])
                    if num == json_len:
                        server.start()
                        while True:
            #request massege snad and data pull
                            RequestData(sensor)
                            time.sleep(1)
else:
    print("not data")
    time.sleep(0.5)
