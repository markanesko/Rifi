'''
Made by Aayush Pokharel

Last modified on: Feb 16, 2020

https://github.com/Aayush9029

'''

from pyautogui import press
from flask import Flask, render_template, request
from random import randint
from time import sleep
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80)) #this sees if device is connected to internet
ip = s.getsockname()[0]
s.close()

#this finds the current local ip of the machine
port_num = randint(49152,65535) # generates a random port  

print('-'*10)
print(f"\n\n\n\n\n Type this in Apple watch app =>  {ip}:{port_num}\n\n\n\n")
print('-'*10)
app = Flask(__name__)
@app.route("/")
def index():
    # query is key and the default value is None
    key = request.args.get("key", "None")

    render_template("index.html", key=key)


    # presses key as it receives via GET
    # I Know this is the worst way of error handling "feel free to sugesst any improvement"
    try:
        press(key)
        sleep(0.3)
    except:
        pass

    
    # this step is kinda reduntant for now
    return render_template("index.html", key=key)

# change the port to any number 8000 to 65535 
app.run(host="0.0.0.0", port=port_num)
