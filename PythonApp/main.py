'''
Made by Aayush Pokharel

Project Started on: Feb 16, 2020

https://github.com/Aayush9029

'''

from pyautogui import press
from flask import Flask, render_template, request
from random import randint
from time import sleep
import socket
import qrcode
from PIL import Image

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # this sees if device is connected to internet
ip = s.getsockname()[0]
s.close()

# port_num = randint(49152, 65535)  # generates a random port

port_num = 8000

ask = input("do you want to see the qr Code? ")
if ask.lower() == 'y' or ask.lower() == 'yes':
    qrCode = qrcode.make(f"http://{ip}:{port_num}")
    qrCode.show()
print('-'*10)
print(f"\n\n\n\n\n Type this in Apple watch app =>  {ip}:{port_num}\n\n\n\n")
print('-'*10)
app = Flask(__name__)
@app.route("/")
def index():

    return render_template("index.html")


@app.route("/press")
def do_press():
    # query is key and the default value is None
    key = request.args.get("key", "None")

    # presses key as it receives via GET
    success = True
    try:
        press(key)
        sleep(0.3)
    except:
        success = False

    return {"press": success}


# change the port to any number 8000 to 65535
app.run(host="0.0.0.0", port=port_num)
