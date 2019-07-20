import webbrowser
import cv2
import paho.mqtt.client as mqttClient
import time
import subprocess

Connected = False

def show_webcam(payload):
    if (payload == 1):
        p = subprocess.Popen(["chromium-browser", "--no-sandbox", "--kiosk", "--test-type", "http://CAMERAFEEDURL:PORT",])  #### Edit for your camera url
    if (payload == 0):
        p = subprocess.Popen(["killall", "chromium-browse",])
        p = subprocess.Popen(["chromium-browser", "--no-sandbox", "--kiosk", "--test-type", "--app=http://RETURNURL.COM",]) ### Edit url

def on_message(client, userdata, message):
    print "Message received: "  + message.payload
    process_trigger(message.payload)

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def process_trigger(payload1):

    if (payload1 == 'ON'):
        print "Opening webcam"
        show_webcam(1)

    if (payload1 == 'OFF'):
        print "Closing webcam"
        show_webcam(0)

broker_address= "broker_ip_here"
port = 1883
user = "username"
password = "password"

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect                      #attach function to callback
client.on_message = on_message                      #attach function to callback

client.connect(broker_address, port=port)  #connect to broker
client.loop_start()                        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("pi/door/motion")


try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
